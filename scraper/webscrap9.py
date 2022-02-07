# video sajjad: webscraping video 004 introduction to python
import requests
from bs4 import BeautifulSoup

# scraping this url to get the whole text of this web site:

url = 'https://biography.yourdictionary.com/articles/how-did-bruce-lee-die.html'
# to check if the url is valid or not , if 200 ==> valid
# 1- Request and check response
response = requests.get(url)
# print(response)

# 2- Parsing:
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify())
# print(soup.find('p').text) # or
paragraph = soup.p.text
# print(paragraph)

# to add something to this paragraph (which is a string):
updated_para = paragraph + '(Parsed)'
# print(updated_para)

# to print the whole paragraph in the url:
paras = soup.findAll('p')  # it is a list.
# to print the whole texts without p tags included, we need to use for loop to iterate in list:

for p in paras:
    print(p.text)
