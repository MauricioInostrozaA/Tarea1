import time
import string
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver =  webdriver.Chrome('C:\Selenium\chromedriver.exe') 
#Recovering Pass
driver.get("https://www.emp-online.es/passwordresetdialog")
time.sleep(5)
webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
time.sleep(2)
##email
usr = driver.find_element_by_id("dwfrm_requestpassword_email")
usr.clear()
usr.send_keys("fake0290.3@yahoo.com")
sendButton = driver.find_element_by_xpath('//*[@id="PasswordResetForm"]/fieldset/div/div/button')
driver.execute_script("arguments[0].click();", sendButton)
