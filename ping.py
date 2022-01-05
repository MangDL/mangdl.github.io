import json
import time
from multiprocessing.pool import ThreadPool
from operator import itemgetter

import httpx
import yaml
from icmplib import ping
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
        for i in zip(["manga", "chapter", "dl_search"]):
            getattr(prov, i)
        test = True
        print([url, test])
    except:
        test = False

    try:
        p = ping(URL(url).host, count=4, privileged=False)
        alive = p.is_alive
        stat = alive and test
        avg = p.avg_rtt
    except:
        alive = False
        stat = False
        avg = 0

    op[k] = {
        "url": url,
        "stat": stat,
        "ol": alive,
        "test": test,
        "ping": avg,
        "ud": int(time.time()),
        "notes": " ".join(notes),
        "pf": vm.get(pf, pf) or "N/A",
        "flag": v.get("flag", [])
    }

with ThreadPool(30) as pool:
    pool.map(fping, fyml["sites"].items())
    pool.close()
    pool.join()

httpx.post(kv_url, json={"all": json.dumps(dict(sorted(op.items(), key=itemgetter(0))), indent=None)})