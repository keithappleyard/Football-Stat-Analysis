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
headers = [header.text for header in table.find('thead').find('tr', class_=lambda x:x != 'over_header').findAll('th') if header.get('data-stat') != 'ranker']

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

#Write goalkeeper stats
with open("Goalkeepers.csv", mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    for data in positions['Goalkeepers']:
        print(data)
        writer.writerow(data)

#Write defender stats
with open("Defenders.csv", mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    for data in positions['Defenders']:
        print(data)
        writer.writerow(data)

#Write midfielder stats
with open("Midfielders.csv", mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    for data in positions['Midfielders']:
        print(data)
        writer.writerow(data)

#Write forward stats
with open("Forwards.csv", mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    for data in positions['Forwards']:
        print(data)
        writer.writerow(data)