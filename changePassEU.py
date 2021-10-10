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
usr = driver.find_element_by_xpath("//input[starts-with(@id,'dwfrm_login_username_d0')]")
usr.clear()
usr.send_keys("error0290.3@gmail.com")
#//*[@id="dwfrm_login_password_d0vxvqptffvb"]
psw = driver.find_element_by_xpath("//input[starts-with(@id,'dwfrm_login_password_d0')]")
psw.send_keys("Loremipsum0180@*")
clk = driver.find_element_by_id("loginButton").click()
time.sleep(2)
###
clk2 = driver.find_element_by_xpath('//*[@id="primary"]/div[1]/div/div[2]/div/div[1]/a').click()
time.sleep(2)
## "Cambiar tu Contraseña"Button
element = driver.find_element_by_xpath('//*[@id="primary"]/div/div/label')
driver.execute_script("arguments[0].click();", element)
##oldpass
oldPass = driver.find_element_by_xpath("//input[starts-with(@id,'dwfrm_profile_login_currentpassword_d0')]")
oldPass.send_keys("Loremipsum0180@*")
##new pass
newPass = driver.find_element_by_xpath("//input[starts-with(@id,'dwfrm_profile_login_newpassword_d0')]")
newPass.send_keys("Loremipsum0180@*")
##new pass confirmation
newPassConf = driver.find_element_by_xpath("//input[starts-with(@id,'dwfrm_profile_login_newpasswordconfirm_d0')]")
newPassConf.send_keys("Loremipsum0180@*")
## send
clk4 = driver.find_element_by_xpath('//*[@id="ChangePassowrdForm"]/fieldset/div/div[4]/button')
driver.execute_script("arguments[0].click();", clk4)