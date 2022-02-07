# video sajjad: video 008 scraping pictures from YTS (websire): https://yts.mx/browse-movies
import requests
import urllib.request
from bs4 import BeautifulSoup

# 1-Requesting
url = 'https://yts.mx/browse-movies'
response = requests.get(url)
# print(response)  # to check if the site is ok

# 2-parsing:
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify)
frames = soup.findAll(
    'div', class_='browse-movie-wrap col-xs-10 col-sm-4 col-md-5 col-lg-4')
# print(frames)
# 3-image of filtering:
for frame in frames:
    try:
        figure = frame.find('figure')
        photo_url = figure.img['src']
        # print(photo_url)
    # parsing the name of the movie photo
        name = photo_url.split('/')
        name = name[-2] + name[-1] # name[-2] = name of the film + name[-1] = extension jpg ==> the link is a list
        # print(name)
    # downloading the pictures:
        print(urllib.request.urlretrieve(photo_url, name))
    except urllib.error.HTTPError:
        print(f'!!! {name} image not found.')
