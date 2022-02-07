# video sajjad: video 007
# scraping ICC site to get top top 10 teams:
import requests
from bs4 import BeautifulSoup

url = 'https://www.icc-cricket.com/rankings/mens/team-rankings/test'
response = requests.get(url)
# print(response) # it should give 200 which means it is ok
# or use : 'lxml' instead of html.parser

# parsing:
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify())
# country = soup.find('span', class_='u-hide-phablet')
# print(countries.text)

# excracting only countries:
# countries = soup.findAll('span', class_='u-hide-phablet')
# for count in countries:
#    print(count.text)

# parsing the name of the countries from table since we have 1 table we will use find instead of findAll:
table = soup.find(
    'div', class_='rankings-block__container full rankings-table')
# print(table)
# excrating name of coutries from the table:
'''
rank = 1
for team in table.findAll('span', class_='u-hide-phablet'):
    print(rank, end='- ')
    print(team.text)
    rank += 1
'''
# or
rank = 1
for team in table.findAll('span', class_='u-hide-phablet'):
    name = team.text.replace(' ', '')   # to eliminate spaces
    name = team.text.replace('\n', '')  # to eliminate lines
    print(str(rank) + ' -' + name)
    rank += 1
