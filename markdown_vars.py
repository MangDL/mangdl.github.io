import base64
from datetime import date

from src.settings import stg

ASSETS = "./docs/assets"
IMAGES = f"{ASSETS}/images"
FOLDER = stg('folder')

def b64(name: str):
    with open(f"./docs/assets/images/icons/{name}", "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


def todo():
    str_repl = {
        "TODO\n====": "## TODO",
        "## Main": "### Main",
        "## Side": "### Side",
        "## Done": "### Done",
    }

    with open(f"docs/TODO.md", "r") as file:
        f = file.read()
        for r in str_repl:
            f = f.replace(r, str_repl[r])
        return f


class Vars:
    # Commons
    # constants
    project_name = "MangDL"
    organization = project_name
    user = "whinee"
    site = "mdl.pages.dev"
    dc_acc = "whi_ne#5135"
    dc_link = "https://discord.com/users/867696753434951732"
    dc_inv = "JbAtUxGcJZ"
    dc_serv = 889508240495366184
    python_ver = "3.10.0"
    os = "Arch Linux"
    # variables
    repo_name = project_name.replace(" ", "-")
    year = str(date.today().year)

    # README.md
    # constants
    title = "MangDL"
    # variables
    TODO = todo()

    # terminal.html
    # constants
    username = "whi~nyaan"
    compname = "blackspace"


icons = ["issues", "forks", "stars", "contributors", "license", "code", "discord"]
for i in icons:
    setattr(Vars, f"{i}_b64", b64(f"{i}.png"))
