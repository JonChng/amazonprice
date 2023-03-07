
from bs4 import BeautifulSoup
import requests
import lxml




url = "https://www.amazon.com/SteelSeries-Compact-Mechanical-Gaming-Keyboard/dp/B07TGQ7CNF/ref=sr_1_1_sspa?keywords=gaming+keyboard&pd_rd_r=5ade629c-7939-453a-b64f-29dc78371696&pd_rd_w=fagDc&pd_rd_wg=DII28&pf_rd_p=12129333-2117-4490-9c17-6d31baf0582a&pf_rd_r=AH4YDEPSTB90AP8VQE19&qid=1678199275&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEySEVJM1daNlQxM05WJmVuY3J5cHRlZElkPUEwNjYwMzMyMk5NUEpIQ0E5WVpWRCZlbmNyeXB0ZWRBZElkPUEwODI4NTY2MjlJOFZaSlhKOVY4UyZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="

headers = {
    "Accept-Language":"en-GB,en;q=0.7",
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
}

# response = requests.get(url=url, headers=headers)
# response.raise_for_status()
#
#
# response.encoding = "utf-8"
# soup = BeautifulSoup(response.content, "lxml")
# print(soup)

def lovely_soup(url):
    r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1'})
    return BeautifulSoup(r.content, 'lxml')


soup = lovely_soup(url)