import io
import os
import re
import shlex
import shutil
import subprocess
from os import mkdir
from os.path import realpath
from typing import Any, Dict

import bs4 as bs
import requests
from lxml import etree
from PIL import Image
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from .settings import stg
from .utils import dict_extr, dict_merge, req_net

FOLDER = stg("folder")

HEADER = """<!DOCTYPE html>
<html lang="en">

<head>
    <title>Terminal</title>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width,initial-scale=1" />
    <meta name="description" content="" />
    <link rel="stylesheet" href="prism.css" />
    <style type="text/css">
        div pre code {
            background-color: #232627;
            color: white;
            display: block;
            padding: 5px;
            inline-size: 1000px;
            white-space: pre-wrap;
            word-break: break-all;
        }
        div {
            background-color: #232627;
            inline-size: 1000px;
        }
    </style>
</head>

<body>"""

RULES_YAML = "/".join([*realpath(__file__).split("/")[:-1], "rules.yaml"])
TERMINAL_TOML = "/".join([*realpath(__file__).split("/")
                         [:-1], "terminal.toml"])
TERMINAL_HTML = "/".join([*realpath(__file__).split("/")
                         [:-2], "docs/assets/images/terminal.html"])


def repl(term: str, cmd: str, cmdp_op: str, add: list[Any] | tuple[Any] = ()) -> str:
    re_ls = stg(f"{term}/colors/re", RULES_YAML)
    sub_ls = stg(f"{term}/colors/sub", RULES_YAML)
    repl = (
        *[(o, n)
          for o in stg(f"{term}/colors/sub", RULES_YAML) for n in sub_ls[o]],
        *[(match.group(), f'<span style="color:#{c};">{match.group()}</span>') for c in re_ls
          for p in re_ls[c] for match in re.finditer(p if p else "", cmd, re.MULTILINE)],
        *[(i, "") for i in stg(f"{term}/rm", RULES_YAML) if i is not None],
        *[i for i in stg(f"{term}/repl", RULES_YAML).items()
          if i[0] is not None],
        *[[f'${{{o}}}', n] for o, n in stg("alias", TERMINAL_TOML).items()],
    )
    for o, n in repl + tuple(add):
        if o:
            cmdp_op = cmdp_op.replace(o, n)
    return cmdp_op


class Terminals:
    bg = "#232627"
    border = 30

    border = f"{border}x{border}"

    def __init__(self, tdict: Dict[str, Any]):
        self.tdict = tdict

    def fish(self):
        comment = ""
        funamepwd = f'<span style="color:#1cdc9a;">{self.tdict["username"]}</span>@{self.tdict["compname"]}<span style="color:#11d116;"> {self.tdict["pwd"]}</span>>'
        unamepwd = re.sub(r"<[^>]+?>", "", funamepwd)
        cmdp_ops = []
        for cmdp in self.tdict["cmdps"]:
            scmd = cmdp["cmd"].split("\n")
            for i, c in enumerate(scmd):
                fw = c.split(" ", 1)[0]
                scmd[i] = c.replace(
                    fw, f'<span style="color:#005fd7;">{fw}</span>', 1)
            cmd = f'\n{" " * (len(unamepwd) + 1) if self.tdict["indented"] else ""}'.join(
                scmd)
            cmd = repl(
                term=self.tdict["terminal"],
                cmd=cmd,
                cmdp_op=cmd,
            )
            cmdp_ops.append(
                f'{funamepwd} <span style="color:#00afff;">{cmd}</span>\n{cmdp["op"]}')
        return (comment, "\n".join(cmdp_ops))

    def windows_powershell(self):
        comment = "<!-- HTML generated using https://hilite.me, modified by me(https://github.com/whitespace-negative) -->"
        unamepwd = f'PS {self.tdict["pwd"]}>'
        funamepwd = unamepwd
        cmdp_ops = []
        for cmdp in self.tdict["cmdps"]:
            cmd = f'\n{" " * (len(unamepwd) + 1) if self.tdict["indented"] else ""}'.join(
                cmdp["cmd"].split("\n"))
            parameters = {
                "code": cmd,
                "lexer": "powershell",
                "style": "default",
                "divstyle": "",
            }
            resp = requests.get(url="http://hilite.me/api",
                                params=parameters).text
            cmdp_op = "".join([
                "", *[
                    etree.tostring(i).decode("utf-8")
                    for i in etree.HTML(resp).xpath("//div/pre/span")
                ]
            ])
            soup = bs.BeautifulSoup(cmdp_op, features="html.parser")
            sdel = [
                ["color: #008000; font-weight: bold", "color:#f9f1a5;"],
                ["border: 1px solid #FF0000", None],
            ]
            for o_s, n_s in sdel:
                for x in soup.select('[style="{}"]'.format(o_s)):
                    if x:
                        x['style'] = n_s
                    else:
                        x['id'] = "del"
            cmdp_op = str(soup)
            for o, n in [(str(i), i.text) for i in soup.findAll(id="del")]:
                cmdp_op = str(cmdp_op).replace(o, n)
            cmdp_op = repl(
                term=self.tdict["terminal"],
                cmd=cmd,
                cmdp_op=str(cmdp_op),
            )
            cmdp_ops.append(f'{funamepwd} {cmdp_op}{cmdp["op"]}')
        return (comment, "\n".join(cmdp_ops))


@req_net
def update():
    term = stg(None, TERMINAL_TOML)
    terminals = []
    for id in term["terminals"]:
        cb = []
        tdict = term["terminals"][id]
        title = f'{tdict["os_family"]}({tdict["os"]}) - {tdict["terminal"]}{"(Administrator)" if tdict["admin"] else ""}'
        com, cb = getattr(Terminals(dict_merge(tdict, dict_extr(term, ["username", "compname"]))),
                          tdict["terminal"].lower().replace(" ", "_"))()
        com = f"{com}\n" if com else ""
        fdiv = f'{com}<div id="{id}"><pre><code><span style="font-weight:1000">{title}</span>\n\n{cb}</code></pre></div>'
        for o, n in stg("alias", TERMINAL_TOML).items():
            fdiv = fdiv.replace(f'${{{o}}}', n)
        terminals.append(fdiv)
    with open(TERMINAL_HTML, "w") as f:
        terminals = "\n\n".join(terminals)
        f.write(
            f"{HEADER}\n\n{terminals}\n<script src=\"prism.js\"></script>\n</body>\n</html>")
    options = Options()
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-application-cache")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--headless")
    driver = webdriver.Firefox(executable_path=r"./src/geckodriver/geckodriver",
                               options=options)
    driver.get(f'file://{TERMINAL_HTML}')
    driver.fullscreen_window()
    try:
        mkdir("./docs/assets/images/cache/")
    except FileExistsError:
        pass
    for i, elem in enumerate(driver.find_elements_by_xpath("/html/body/div")):
        Image.open(
            io.BytesIO(
                driver.find_element_by_xpath(f"/html/body/div[{i + 1}]").screenshot_as_png)).save(
                    f"./docs/assets/images/cache/{elem.get_attribute('id')}.png")
    driver.quit()
    subprocess.run(shlex.split(
        f"mogrify -trim ./docs/assets/images/cache/*.png"))
    subprocess.run(
        shlex.split(
            f'mogrify -bordercolor "{Terminals.bg}" -border {Terminals.border} -path ./docs/assets/images ./docs/assets/images/cache/*.png'
        ))
    os.remove("./docs/assets/images/terminal.html")
    shutil.rmtree("./docs/assets/images/cache/")
    shutil.rmtree(f"../{FOLDER}/docs/assets/images")
    shutil.copytree("./docs/assets/images", f"../{FOLDER}/docs/assets/images")
