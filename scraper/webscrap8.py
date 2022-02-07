import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=34.09969000000007&lon=-118.33512999999999')
# soup = BeautifulSoup(page, 'lxml')
soup = BeautifulSoup(page.content, 'html.parser')
#ex: finding all the links on the page:
# print(soup.findAll('a'))

week = soup.find(id='seven-day-forecast-list')
# print(week)
items = week.findAll(class_='tombstone-container')
# print(items[0])
'''
print(items[1].find(class_='period-name').get_text())
print(items[1].find(class_='short-desc').get_text())
print(items[1].find(class_='temp').get_text())
'''
#---------------------------------------
period_names = [item.find(class_='period-name').get_text() for item in items[1:]]
short_descriptions = [item.find(class_='short-desc').get_text() for item in items[1:]]
temperatures = [item.find(class_='temp').get_text() for item in items[1:]]
# print(period_names[1:])
# print(short_descriptions[1:])
# print(temperatures[1:])

weather_stuff = pd.DataFrame(
    {
        'Period_names': period_names,
        'Short_descriptions': short_descriptions,
        'Temperatures': temperatures
    })
print(weather_stuff)
weather_stuff.to_csv('weather.csv') # will write results to excek file weather.csv










