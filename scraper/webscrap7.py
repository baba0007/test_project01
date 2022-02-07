#we will extract contents, urls, and tables from this website:
# https://pythonprogramming.net/parsememcparseface/
from bs4 import BeautifulSoup as bs
import requests
import urllib.request
import pandas as pd

# source = requests.get('https://pythonprogramming.net/parsememcparseface/').text
# soup = bs(source, 'lxml')
# print(soup.title.string) # or print(soup.title.text)
# print(soup.p.text) # will print the first paragraph of the site.
# print(soup.findAll('p'))

# for paragraph in soup.findAll('p'):
#    print(paragraph.text)

# print(soup.getText()) # get all the text of the web
# to get all the link of the web:
# for url in soup.findAll('a'):
#    print(url.get('href'))

# nav = soup.nav # nav = navigation bar of the website:
# print(nav)
# for url in nav.findAll('a'):
#    print(url.get('href'))

# finding paragraph in body:
# body = soup.body
# for paragraph in body.findAll('p'):
#    print(paragraph.text)

# find all texts between div tags:
# for div in soup.findAll('div', class_='body'):
#   print(div.text)

#1- tables:
# table = soup.table
# or
# table = soup.find('table')
# print(table)
# table_rows = table.findAll('tr')
# for tr in table_rows:
#    td = tr.findAll('td') # td = table data, tr=table row
#    row = [i.text for i in td]
#    print(row)
    
#to grab table also we use pandas:
# will go to all tables in this website and return as data frames dfs:
# dfs = pd.read_html('https://pythonprogramming.net/parsememcparseface/')
# for df in dfs: # for df = data in dataframes = dataframes
#    print(df)

#2-xml it is in the sitemap in this this website example:

source = urllib.request.urlopen('https://pythonprogramming.net/sitemap.xml').read()
soup = bs(source, 'xml')

for url in soup.findAll('loc'):
    print(url.text)
    

