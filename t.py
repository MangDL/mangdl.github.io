from src.settings import stg
from yarl import URL

yml = stg(None, "rejected.yaml")
flag = yml["flag"]
sites = yml["sites"]

mdb = """<h1 align="center" style="font-weight: bold">
    LIST OF REJECTED SITES
</h1>

A site will not be accepted if it:
- does not have a list of all comics
- has duplicate links
- has external links redirecting to other sites
- has no search capability
- is geo-blocked
- is protected by an anti-DDoS mechanism except for DDoS Guard
- is torrent and/or download only; and
- serves paid content

| Site | Reason/s |
|:---:|:---:|"""

op = []

for k, v in sites.items():
    j = []
    for i in v:
        j.append(flag[i])
    op.append([f'<a target="_blank" href="{k}">{URL(k).host}</a>', ", ".join(j)])

with open("docs/_rejected.md", "w") as f:
    md = []
    for i in op:
        md.append(f'| {" | ".join(i)} |')
    f.write("{}\n{}".format(mdb, '\n'.join(md)))