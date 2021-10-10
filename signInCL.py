import time
import string
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver =  webdriver.Chrome('C:\Selenium\chromedriver.exe') 
driver.get("https://tempmailo.com/")
time.sleep(5)
#button change
click1 = driver.find_element_by_xpath('//*[@id="apptmo"]/div/div[1]/div[2]/div[3]/button').click()
#button ok
click2 = driver.find_element_by_xpath('//*[@id="apptmo"]/div[2]/div/div[3]/button[1]').click()
time.sleep(5)
#button copy
click3 = driver.find_element_by_xpath('//*[@id="apptmo"]/div/div[1]/div[1]/div/button').click()
driver.get("https://www.ebest.cl/customer/account/create/")
time.sleep(5)
letters_n_digits = string.ascii_lowercase + string.digits
##
fname = driver.find_element_by_id("firstname")
fname.clear()
fname.send_keys("0290")
##
lname = driver.find_element_by_id("lastname")
lname.clear()
lname.send_keys("3")
##
usr = driver.find_element_by_id("email_address").send_keys(Keys.CONTROL, "v")
##
psw = driver.find_element_by_id("password")
str = ''.join(random.choice(letters_n_digits) for i in range(8)) + '@'
psw.send_keys(str)
psw_conf = driver.find_element_by_id("password-confirmation")
psw_conf.send_keys(str)
print("password: " + str)
clk = driver.find_element_by_xpath('//*[@id="form-validate"]/div/div[1]/button').click()