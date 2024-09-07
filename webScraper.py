import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
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
options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
url = 'https://fbref.com/en/comps/9/stats/Premier-League-Stats'
driver.get(url)
time.sleep(5)

#Scrape the data
data = driver.page_source
soup = BeautifulSoup(data, 'html.parser')
table = soup.find('table', id='stats_standard')
driver.quit()

#Extract headers from table
headers = [header.text for header in table.find('thead').findAll('th')]

#Extract player data
for player in table.findAll('tr', class_=lambda x: x != 'thead'):
    data = [data.text for data in player.findAll('td')]
    if(data):
        if('GK' in data[2]):
            positions['Goalkeepers'].append(data)
        elif('DF' in data[2]):
            positions['Defenders'].append(data)
        elif('MF' in data[2]):
            positions['Midfielders'].append(data)
        elif('FW' in data[2]):
            positions['Forwards'].append(data)

