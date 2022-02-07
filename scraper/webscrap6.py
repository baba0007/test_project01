#video = https://www.youtube.com/watch?v=GjKQ6V_ViQE
from bs4 import BeautifulSoup as bs
import requests

r =  requests.get('https://keithgalli.github.io/web-scraping/example.html').text
# convert to BeautifulSoup object:
soup = bs(r, 'lxml')
#finding link:
# print(soup.a.text)
# searching for h1 and h2 tags:
# headers = soup.findAll(['h1', 'h2'])
# print(headers)
# finding all p tags:
# paragraph = soup.find_all('p', attrs={'id':'paragraph-id'})
# print(paragraph)
# finding body:
body = soup.find('body')
# print(body)
#finding all div tags in that body:
div = body.find('div')
# print(div)
#finding h1 in that div:
h1 = div.find('h1')
# print(h1)

# find some text :
text = soup.findAll('p', string='Some bold text')
print(text)

