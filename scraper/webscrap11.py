# video sajjad: video 007
# scraping ICC site to get top top 10 teams:

import requests
from bs4 import BeautifulSoup

url = 'https://www.icc-cricket.com/rankings/mens/team-rankings/test'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find(
    'div', class_='rankings-block__container full rankings-table')
rank = 1
for team in table.findAll('span', class_='u-hide-phablet'):
    name = team.text.replace(' ', '')
    print(f' {str(rank)} -{name}')
    rank += 1
