import time
import string
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver =  webdriver.Chrome('C:\Selenium\chromedriver.exe') 
driver.get("https://www.ebest.cl/customer/account/forgotpassword/")
time.sleep(5)
##
usr = driver.find_element_by_id("email_address")
usr.clear()
usr.send_keys("fake0290.3@yahoo.com")
clk = driver.find_element_by_xpath('//*[@id="form-validate"]/div/div[1]').click()