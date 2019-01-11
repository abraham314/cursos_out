# a class="result-image"

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome('/home/abraham/Descargas/chromedriver')

def login_and_search():	


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

	# driver.quit()

	return driver


def get_detail_link(link_list):

	detail_link = []

	for link in link_list:

		driver.get(link)

		soup = BeautifulSoup(driver.page_source, 'lxml')

		for a in soup.find_all('a', class_ = 'search-result__result-link ember-view'):
			print(a['href'])
			detail_link.append(a['href'])

	return detail_link



def get_page_links():
	
	soup = BeautifulSoup(driver.page_source, 'lxml')	

	link_list = []

	# add the current link, page 1 to list
	link_list.append(driver.current_url)
	print driver.current_url

	ul = soup.find('ul', class_='pagination')

	# not get the final link
	for a in ul.find_all('a')[0:(len(ul.find_all('a'))-2)]:
		print('https://www.linkedin.com' + a['href'])
		link_list.append('https://www.linkedin.com' + a['href'])	

	print '\n'
	print '\n'
	print '\n'

	return link_list



########################################### MAIN ###################################

login_and_search()

get_detail_link(get_page_links())

driver.quit()

####################################################################################


