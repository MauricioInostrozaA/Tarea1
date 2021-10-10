import time
import string
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver =  webdriver.Chrome('C:\Selenium\chromedriver.exe') 
#getting an Email
driver.get("https://tempmailo.com/")
time.sleep(5)
#button change
click1 = driver.find_element_by_xpath('//*[@id="apptmo"]/div/div[1]/div[2]/div[3]/button').click()
#button ok
click2 = driver.find_element_by_xpath('//*[@id="apptmo"]/div[2]/div/div[3]/button[1]').click()
time.sleep(5)
#button copy
click3 = driver.find_element_by_xpath('//*[@id="apptmo"]/div/div[1]/div[1]/div/button').click()
#Register to the site
driver.get("https://www.emp-online.es/register")
time.sleep(5)
webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
time.sleep(2)
letters_n_digits = string.ascii_lowercase + string.digits
##gender
gender = driver.find_element_by_xpath('//*[@id="js-billing-gender-data"]/div/div/label[1]/span').click()
##name
fname = driver.find_element_by_id('dwfrm_profile_customer_firstname')
fname.clear()
fname.send_keys("0290")
##lastname
lname = driver.find_element_by_id("dwfrm_profile_customer_lastname")
lname.clear()
lname.send_keys("3")
##email
usr = driver.find_element_by_id("dwfrm_profile_customer_email").send_keys(Keys.CONTROL, "v")
##confirm email
usr2 = driver.find_element_by_id('dwfrm_profile_customer_emailconfirm').send_keys(Keys.CONTROL, "v")
##password
psw = driver.find_element_by_xpath("//input[starts-with(@id,'dwfrm_profile_login_password_d0')]")
str = "Loremipsum0180@*"
psw.send_keys(str)
##password confirm 
psw_conf = driver.find_element_by_xpath("//input[starts-with(@id,'dwfrm_profile_login_passwordconfirm_d0')]")
psw_conf.send_keys(str)
print("password: " + str)
element = driver.find_element_by_xpath('//*[@id="dwfrm_profile_customer_acceptterms"]')
driver.execute_script("arguments[0].click();", element)
saveButton = driver.find_element_by_xpath('//*[@id="RegistrationForm"]/fieldset[5]/div[2]/button')
driver.execute_script("arguments[0].click();", saveButton)