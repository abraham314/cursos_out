from selenium import webdriver
from bs4 import BeautifulSoup

# create driver
driver = webdriver.Chrome('/home/abraham/Descargas/chromedriver')

url = 'http://stats.nba.com/players/list/'

# download html page
driver.get(url)

# print driver.page_source

# create soup
soup = BeautifulSoup(driver.page_source, 'lxml')

div = soup.find('div', class_= "stats-player-list players-list")

#print(div)

for a in div.find_all('a'):
	print(a.text)

driver.quit()
