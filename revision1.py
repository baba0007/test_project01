# extract links from a web page and count it:
'''
import requests
from bs4 import BeautifulSoup

host = input('Page to check: ')
req = requests.get(host)
data = req.text

real_stuff = BeautifulSoup(data, 'html.parser')

counter = 0
for x in real_stuff.find_all('a'):
    print(x.get('href'))
    counter += 1
print()
print('Number of links: ', counter)
'''
#-----------------------------
# How to ping Multiple IP Adresses:
'''
import os

ip = '11.0.0.'
for x in range(100, 121):
    result = os.popen('ping -c 1 ' + ip + str(x))

    for line in result.readlines():

        if line.count('ttl'):
            print(ip + str(x), '---> Live')
'''
# -----------

x = ['ab', 'cd']
y = ['ab', 'cd']

for i in x:
    y.append(i.upper())
print(y)

# ------------
print()
for i in range(5):
    print((i + 1) * '* ')
# ---------------
