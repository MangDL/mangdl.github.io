import importlib
import os
from pathlib import Path

import httpx
import pdoc
import yaml
from bs4 import BeautifulSoup
from mako.lookup import TemplateLookup
from selenium_driver_updater import DriverUpdater

import markdown_vars
from src import terminal
from src.settings import stg

FOLDER = stg("folder")

def main():
    # DriverUpdater.install(
    #     path = "./src/geckodriver",
    #     driver_name = DriverUpdater.geckodriver,
    #     upgrade = True,
    #     check_driver_is_up_to_date = True,
    # )
    # terminal.update()
    importlib.reload(markdown_vars)
    Vars = markdown_vars.Vars

    with open("license.yaml", "r") as f:
        license = yaml.load(f.read(), yaml.FullLoader)
    if (copyright := []) == []:
        c = license["cholder"]
        for u, (r, y) in ((*u.keys(), *r.items()) for u in c for s in u.values() for r in s):
            copyright.append(
                f"by [Github Account [{u}](https://github.com/{u}) Owner, {y}] as part of project [{r}](https://github.com/{u}/{r})"
            )
        if len(copyright) > 1:
            copyright[-2] += f", and {copyright[-1]}"
            del copyright[-1]
        cholder = f"""Copyright for portions of project [{Vars.project_name}](https://github.com/{Vars.project_name}/{Vars.repo_name}) are held {', '.join(copyright)}.\n
All other copyright for project [{Vars.project_name}](https://github.com/{Vars.user}/{Vars.repo_name}) are held by [Github Account [{Vars.user}](https://github.com/{Vars.user}) Owner, 2021]."""
    else:
        cholder = f"Copyright (c) 2021 Github Account [{Vars.project_name}](https://github.com/{Vars.user}) Owner"
    Vars.conditions = ("" if license["conditions"][0] is None else "\n" + "\n\n".join(license["conditions"]) + "\n")
    Vars.cholder = cholder

    pdoc.tpl_lookup = TemplateLookup(
        cache_args=dict(cached=True, cache_type='memory'),
        input_encoding='utf-8',
        directories=["./docs/template/"],
    )
    os.mkdir(FOLDER)
    _html = pdoc.Module(FOLDER, context=pdoc.Context()).html()
    os.rmdir(FOLDER)
    for tpl in list(Path(".").rglob("_*.md")):
        spl = str(tpl).split("/")
        file = os.path.join(*spl[:-1], spl[-1][1:].split(".")[0])
        RM = spl[-1][1:].split(".")[0] == "README"
        with open(tpl, "r") as fin, open(f'../{FOLDER}/{file}.md', "w") as fout, open(os.path.join(*spl[:-1], 'index.html') if RM else f'{file}.html', "w") as hout:
            tpl_str = fin.read()
            for var in tuple(i for i in dir(Vars) if not i.startswith("__")):
                tpl_str = tpl_str.replace(f"${{{var}}}", str(getattr(Vars, var)))
            fout.write(tpl_str)

            soup = BeautifulSoup(_html, "html.parser")
            headers = {"Content-Type": "text/plain", "charset": "utf-8"}
            md = str(
                httpx.post("https://api.github.com/markdown/raw", headers=headers, data=tpl_str.encode("utf-8")).content,
                encoding="utf-8"
            )

            md_repl = [
                [
                    '[ ]',
                    '<input type="checkbox" disabled="">'
                ],
                [
                    '[x]',
                    '<input type="checkbox" disabled="" checked="">'
                ],
                [
                    '<link href="/github-markdown-css/github-css.css" rel="stylesheet"/>',
                    ''
                ],
                [
                    ".md",
                    ".html"
                ]
            ]

            for o, n in md_repl:
                md = md.replace(o, n)

            repl = [
                [
                    "const url = '../doc-search.html#' + encodeURIComponent(query);",
                    "const url = 'doc-search.html#' + encodeURIComponent(query);"
                ],
                [
                    str(soup.select_one('article#content')),
                    f'<article id="content">{md}</article>'
                ],
                [
                    "user-content-",
                    ""
                ]
            ]

            html = _html
            for o, n in repl:
                html = html.replace(o, n)
            soup = BeautifulSoup(html, "html.parser")
            toc = soup.select_one("h2 a#table-of-contents")
            logo = soup.select_one("img#logo")
            if logo:
                logo["style"] = "display: block; margin: auto;"
            if RM:
                if toc:
                    html = str(soup).replace(str(soup.select_one(".toc")), f'<div class="toc"><ul><li><a href="docs/index.html"><strong>Documentation</strong></a></li><ul></div><h2>Table of Contents</h2><div class="toc">{str(toc.find_next("ul"))}</div>')
            else:
                html = str(soup).replace(str(soup.select_one(".toc")), f'<div class="toc"><ul><li><a href="index.html"><strong>Homepage</strong></a></li><li><a href="docs/index.html"><strong>Documentation</strong></a></li><ul></div>')
            hout.write(html)

if __name__ == "__main__":
    main()
