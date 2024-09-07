from selenium import webdriver
from bs4 import BeautifulSoup
import time

#Dictionaries for each position
positions = {
    'Goalkeepers': [],
    'Defenders': [],
    'Midfielders': [],
    'Forwards': []
}

#Load the website to access dynamically loaded table
driver = webdriver.Chrome()
url = 'https://fbref.com/en/comps/9/stats/Premier-League-Stats'
driver.get(url)
time.sleep(5)

data = driver.page_source
soup = BeautifulSoup(data, 'html.parser')
table = soup.find('table', id='stats_standard')
driver.quit()

playerNames = table.findAll('td', attrs={'data-stat':'player'})
