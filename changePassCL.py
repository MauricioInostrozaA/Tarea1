import time
import string
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver =  webdriver.Chrome('C:\Selenium\chromedriver.exe') 
driver.get("https://www.ebest.cl/customer/account/login/")
time.sleep(5)
##
usr = driver.find_element_by_id("email")
usr.clear()
usr.send_keys("fake0290.3@yahoo.com")
##
psw = driver.find_element_by_id("pass")
psw.send_keys("Loremipsum0180@*")
clk = driver.find_element_by_id('send2').click()
time.sleep(5)
##
changePass = driver.find_element_by_xpath('//*[@id="maincontent"]/div[2]/div[1]/div[3]/div/div[1]/div/a[2]').click()
time.sleep(5)
##
oldPass = driver.find_element_by_id("current-password")
oldPass.send_keys("Loremipsum0180@*")
##
newPass = driver.find_element_by_id("password")
newPass.send_keys("Loremipsum0180@*")
newPassConf = driver.find_element_by_id("password-confirmation")
newPassConf.send_keys("Loremipsum0180@*")
##
guardar = driver.find_element_by_xpath('//*[@id="form-validate"]/div[2]/div[2]/div[1]/button').click()