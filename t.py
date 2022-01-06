from icmplib import ping
from yarl import URL
print(ping(URL("https://hachirumi.com").host, count=4, privileged=True))