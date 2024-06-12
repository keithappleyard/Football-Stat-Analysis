import requests
from bs4 import BeautifulSoup

#Analyse every team
baseUrl = 'https://fbref.com'
data = requests.get(f'{baseUrl}/en/comps/9/Premier-League-Stats')
soup = BeautifulSoup(data.text, 'html.parser')
table = soup.select('table.stats_table')[0]
teams = table.findAll('td', attrs={'data-stat':'team'})

#Get information about specific team
team = 'Manchester Utd'
teamUrl = ''
for i in teams:
    if i.text.strip() == team:
        teamUrl = i.find('a')['href']

#Load data from specic team
data = requests.get(baseUrl + teamUrl)
soup = BeautifulSoup(data.text, 'html.parser')
table = soup.select('table.stats_table')[0].find('tbody')
players = table.findAll('th', attrs={'data-stat':'player'})
