# video sajjad 010
# making the results is a csv file:
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.icc-cricket.com/rankings/mens/team-rankings/test'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find(
    'div', class_='rankings-block__container full rankings-table')
rank = 1
my_list = []
for team in table.findAll('span', class_='u-hide-phablet'):
    name = team.text.replace(' ', '')
    #print(f' {str(rank)} -{name}')
    my_list.append([rank, name])
    rank += 1
# print(my_list)
# writing each in a column rank and team using pandas:
data_frame = pd.DataFrame(my_list, columns=['Ranking', 'Teams'])
print(data_frame)
# print(data_frame.head()) # will print top 5
# print(data_frame.tail()) # will print last 5
# print(data_frame.tail(2)) # will print the last 2

# writing the file as csv:
data_frame.to_csv('Top 10 test Team.csv')
