import requests

from bs4 import BeautifulSoup


def get_price(entry):
    url = entry.get("url")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }
    content = requests.get(url, headers=headers)

    import pdb

    pdb.set_trace()

    return 666
