from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome('/home/abraham/Descargas/chromedriver')

def login():

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

	time.sleep(3)

	return driver


def get_public_profile_information(url):

	driver.get(url)

	soup = BeautifulSoup(driver.page_source,'lxml')

	# print soup.text
	print(soup.find('span', class_='full-name').text)

	for span in soup.find_all('span', class_ = 'endorse-item-name'):
		print(span.text)

	print('\n')



login()

# sample url for scraping
url = 'https://www.linkedin.com/in/sebasti%C3%A1n-rufino-hern%C3%A1ndez-franch-127a65aa/'

# get name and skill which is endosed
get_public_profile_information(url)

driver.quit()

