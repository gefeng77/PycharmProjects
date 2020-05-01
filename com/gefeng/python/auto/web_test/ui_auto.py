# coding=utf-8
from selenium import webdriver
import time


driver = webdriver.Chrome()
url = "https://www.baidu.com"
driver.get(url)

login = driver.find_element_by_link_text("登录")
login.click()

time.sleep(2)
username_login = driver.find_element_by_xpath('//*[@class="tang-pass-footerBar"]/p[text()="用户名登录"]')
username_login.click()

time.sleep(2)
username = driver.find_element_by_id("TANGRAM__PSP_10__userName")
username.clear()
username.send_keys("gefeng_77")

time.sleep(1)
password = driver.find_element_by_id("TANGRAM__PSP_10__password")
password.clear()
password.send_keys("Xiao@0715")

time.sleep(1)
submit = driver.find_element_by_id("TANGRAM__PSP_10__submit")

submit.click()






