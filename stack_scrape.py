import json
from lxml import html
import requests

URL = "https://travel.stackexchange.com/questions?page=1&sort=newest"

for i in range(1000):
    page = requests.get("https://travel.stackexchange.com/questions?page=" + str(i+1) + "&sort=newest")
    tree = html.fromstring(page.content)
    lis = tree.xpath('//a[@class="question-hyperlink"]/text()')
    with open('data/travel/stackexchange.txt', 'a') as f:
        for i in lis:
            f.write(i + '\n')