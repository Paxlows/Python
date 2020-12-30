from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

name = input("Enter the user name:")
message = input("Enter the message:")
lim = int(input("Enter the limit:"))
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
time.sleep(10)
search = driver.find_element_by_xpath("//*[@id='side']/div[1]/div/label/div/div[2]")
search.send_keys(name)
time.sleep(1)
search.send_keys(Keys.ENTER)
for i in range(lim): 
    driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]").send_keys(message)
    time.sleep(1)
    driver.find_element_by_xpath("""//*[@id="main"]/footer/div[1]/div[3]/button""").click()
driver.quit()
