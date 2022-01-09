import json
import time
from multiprocessing.pool import ThreadPool
from operator import itemgetter

import httpx
import yaml
from mangdl.providers import Provider
from yarl import URL

kv_url = "https://kv.whi-ne.workers.dev"

with open("url.yml", "r") as f:
    fyml = yaml.safe_load(f)
vm = fyml["ac"]
vn = fyml["notes"]

op = {}

def fping(item):
    k, v = item
    url = v["url"]
    host = URL(url).host
    pf = v.get("pf", "")
    notes = []
    nf = vn.get(pf)

    if nf:
        notes.append(nf)
    for i in v.get("flag", []):
        notes.append(vn.get(i))

    try:
        pn, m, ch, dls = v["test"]
        prov = Provider(pn)
        prov.manga(m)
        prov.chapter(ch)
        prov.dl_search(dls)
        for i in ["manga", "chapter", "dl_search"]:
            getattr(prov, i)
        test = True
    except:
        test = False

    pr = httpx.get(f'https://api.justyy.workers.dev/api/ping/?host={host}&cached', timeout=10).text
    if pr == "null":
        ping = 0
        ol = False
    else:
        ping = pr.split(r'\/')[-3]
        ol = True

    op[k] = {
        "url": url,
        "stat": ol & test,
        "ol": ol,
        "test": test,
        "ping": ping,
        "ud": int(time.time()),
        "notes": " ".join(notes),
        "pf": vm.get(pf, pf) or "N/A",
        "flag": v.get("flag", [])
    }
    print(op[k])

with ThreadPool(20) as pool:
    pool.map(fping, fyml["sites"].items())
    pool.close()
    pool.join()

httpx.post(kv_url, json={"all": json.dumps(dict(sorted(op.items(), key=itemgetter(0))), indent=None)})