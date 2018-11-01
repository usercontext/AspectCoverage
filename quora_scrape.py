# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
# from time import sleep
# import json
# import datetime

# driver = webdriver.Safari()
# driver.base_url = "https://www.quora.com/topic/Tourism"
# driver.get(driver.base_url)

# found_questions = driver.find_elements_by_xpath("//span[contains(@class, 'ui_story_title ui_story_title_medium ')]/span/text()")
# print(len(found_questions))
# increment = 10
# # redlen = len(found_questions)
# # prev_ques = []
# prev_len = 0
# tag_lis = ["Tourism",
#            "International Travel",
#            "Visiting and Travel in India",
#            "Vacations",
#            "Hotels",
#            "Air Travel",
#            "Road Trips",
#            "Visiting and Travel in Europe",
#            "Travel Hacks"]
# for i in range(100):
#     print(i)
#     driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
#     prev_len = len(found_questions)
#     sleep(0.3)
#     # found_questions = driver.find_elements_by_xpath("//span[contains(@class, 'ui_story_title ui_story_title_medium ')]/span/text()")
#     # print(i, len(found_questions))


# # print("Ending")
# sleep(10)
# found_questions = driver.find_elements_by_xpath("//span[contains(@class, 'ui_story_title ui_story_title_medium ')]/span/text()")
# found_questions = list(set([i.text for i in found_questions]))
# print(len(found_questions))

# with open('data/travel/quora.txt', 'a') as f:
#     for item in found_questions:
#         f.write("%s\n" % item)
# driver.close()


with open("data/src/quora_tags.txt") as f:
    data = f.readlines()

f = open('data/travel/quora.txt', 'w')
count = 0
for i in data:
    if "Travel" in i or "Tourism" in i or "Vacations" in i or "Hotels" in i or "Trip" in i:
        count +=1
        f.write(i.split()[0] + "\n")

f.close()

print(count)
