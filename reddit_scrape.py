from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from time import sleep
import json
import datetime

driver = webdriver.Safari()
driver.base_url = "https://www.reddit.com/r/travel"
driver.get(driver.base_url)

found_questions = driver.find_elements_by_xpath("//span/a/h2/text()")
print(len(found_questions))
increment = 10
# redlen = len(found_questions)
# prev_ques = []

for i in range(500):
    print(i)
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    # found_questions = driver.find_elements_by_xpath("//span/a/h2/text()")
    # print(i, len(found_questions))
    sleep(0.3)

sleep(10)
found_questions = driver.find_elements_by_xpath("//span/a/h2/text()")
print(len(found_questions))

with open('data/travel/reddit.txt', 'w') as f:
    for item in found_questions:
        f.write("%s\n" % item.text)
driver.close()
