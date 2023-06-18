import requests
from bs4 import BeautifulSoup


def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = "https://www.ebay.com/sch/i.html?_from=R40&_sacat=0&LH_TitleDesc=0&_nkw=fujifilm&_pgn=" + str(page)
        print("Checkpoint 1")
        source_code = requests.get(url)
        print("Checkpoint 2")
        plain_text = source_code.text
        # print(plain_text)
        print("Checkpoint 3")
        soup = BeautifulSoup(plain_text, features="html.parser")
        # for link in soup.findAll('a', {"_sp":"p2351460.m1686.l7400"}):
        for link in soup.findAll('a', {"class":"s-item__link"}):
            print("Checkpoint 4")
            href = link.get("href")
            title = link.text
            print(title)
            print(href)
            global link_count
            link_count += 1
        page += 1

link_count = 0
trade_spider(10)
print("I found", link_count, "links")
