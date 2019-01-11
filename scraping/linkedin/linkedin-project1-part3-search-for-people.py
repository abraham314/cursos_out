# a class="result-image"

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('/home/abraham/Descargas/chromedriver')

driver.get('https://www.linkedin.com/uas/login?goback=&trk=hb_signin')

driver.maximize_window()

email = driver.find_element_by_xpath('//*[@id="session_key-login"]')
email.send_keys('raulabraham.nieto@gmail.com')

time.sleep(3)

password = driver.find_element_by_xpath('//*[@id="session_password-login"]')
password.send_keys('Leslie1210')

time.sleep(3)

login = driver.find_element_by_xpath('//*[@id="btn-primary"]')
login.click()

time.sleep(5)

search = driver.find_element_by_tag_name("input")

#searchx = driver.find_element_by_xpath('//*[@id="jobs-search-box-keyword"]')
search.send_keys("python programmer")
search.send_keys(u"\ue007")
	

time.sleep(3)


people = driver.find_element_by_xpath("//*[starts-with(@id,'ember')]/ul/li[1]/button")
people.click()

time.sleep(10)

#driver.quit()
