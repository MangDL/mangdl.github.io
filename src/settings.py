import json
from os import path
from os.path import abspath as ap
from os.path import dirname as dn
from typing import Any

import toml
import yaml


def readfile(file: str):
    ext = file.split(".")[-1]
    with open(file, "r") as f:
        if ext == "json":
            return json.load(f)
        elif ext == "yaml":
            return yaml.load(f.read(), yaml.FullLoader)
        elif ext == "toml":
            return toml.load(f)


def stg(stg: str, file: str = path.join(dn(ap(__file__)), "settings.yaml")) -> Any:
    op = readfile(file)
    if stg is not None:
        for a in stg.split("/"):
            op = op[a]
    return op


def wr_stg(stg: str, value: Any, file: str = "settings") -> None:
    with open(path.join(dn(ap(__file__)), f"{file}.json"), "r") as f:
        stg_dict = json.loads(f.read())

    def modify(stg: str, value: Any, stg_dict: dict[Any:Any]):
        path_ls = stg.split("/")
        key = path_ls[0]
        if len(path_ls) > 1:
            if isinstance(stg_dict[key], dict):
                modify(stg.replace(f"{key}/", ""), value, stg_dict[key])
            else:
                f_stg = '"]["'.join(stg.split("/")) + ''
                raise Exception(f'["{f_stg}"] at {file}.json not found.')
        else:
            stg_dict[key] = value
            return stg_dict

    modify(stg, value, stg_dict)
    with open(path.join(dn(ap(__file__)), f"{file}.json"), "w") as f:
        json.dump(stg_dict, f, indent=4)
