from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://jarvis.starks.workers.dev/0:/gdriveit_bot/Vikings%20Season%204%20%20(1080p%20BD%20x265%2010bit%20FS84%20Joy)/')
time.sleep(5)

links = driver.find_element_by_class_name("list-group-item-action")
for link in links:
    print(link.text)