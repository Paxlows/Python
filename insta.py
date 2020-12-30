from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# username = 'arunbabuvn@gmail.com' #input("Enter the login Email:") 
# password = 'A!r@U#n$B%a^B&u' #input("Enter the login password:") 
# clint_name = 'juhirus' #input("Enter the user id:")

driver = webdriver.Chrome()
driver.get('https://www.instagram.com/')
time.sleep(2)
class Insta:
    def loginfunc(self,user_name,pass_word):    
        user_name = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        user_name.send_keys(user_name)

        pass_word = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        pass_word.send_keys(pass_word)
        time.sleep(1)

        login = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')
        login.click()
        time.sleep(4)

        not_now = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
        not_now.click()
        time.sleep(1)

        notification = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
        notification.click()

    def searchfunc(self,clint_name):
        time.sleep(2)
        user_search = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div/div')
        user_search.click()
        time.sleep(1)

        user_type = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        user_type.send_keys(clint_name)
        time.sleep(2)

        select_user = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[4]/div/a[1]/div')
        select_user.click()

    def likefunction(self):
        time.sleep(4)
        select_img = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[2]/article/div[1]/div/div[1]/div[1]/a/div')
        select_img. click()
        time.sleep(2)
        like = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button')
        like.click()
        time.sleep(1)
        close_img = driver.find_element_by_xpath('/html/body/div[5]/div[3]/button/div')
        close_img. click()

a = Insta()
a.loginfunc('arunbabuvn@gmail.com',"A!r@U#n$B%a^B&u")
a.searchfunc('juliusdein')
a.likefunction()