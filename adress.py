#import requests
import webbrowser, pyperclip, sys

# page = requests.get('http://thenewboston.com')
# print(page.content)
sys.argv
if len(sys.argv) >  1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()


page = webbrowser.open('https://www.google.nl/maps/search/' + address)
print(page)
