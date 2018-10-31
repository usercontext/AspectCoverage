from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import sys

import unittest
import time
import re
from bs4 import BeautifulSoup as bs
from dateutil import parser
import pandas as pd
import itertools
import matplotlib.pyplot as plt

driver = webdriver.Firefox()
driver.base_url = "https://twitter.com/swyx/following"
driver.get(driver.base_url)

for i in range(1, 230):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    print(i)

html_source = driver.page_source
sourcedata= html_source.encode('utf-8')
soup=bs(sourcedata)
arr = [x.div['data-screen-name'] for x in soup.body.findAll('div', attrs={'data-item-type':'user'})]
bios = [x.p.text for x in soup.body.findAll('div', attrs={'data-item-type':'user'})]
fullnames = [x.text.strip() for x in soup.body.findAll('a', 'fullname')][1:] # avoid your own name
d = {'usernames': arr, 'bios': bios, 'fullnames': fullnames}
df = pd.DataFrame(data=d)
df.to_csv('data/BASICDATA.csv')
