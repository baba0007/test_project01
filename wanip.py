#!/usr/bin/env python3.9
from requests import get
ip = get('https://api.ipify.org').text
#print(f'My Wan IP Address: {ip}')
print('My Wan IP Address is: {}'.format(ip))
