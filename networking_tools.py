#!/usr/bin/env python3

'''
import os


f = None
try:
	Host = input('Enter ip: ') 
	result = os.system(f'ping -c 2 {Host}')
except:
	print('Host Down!!!')
else:
	print('else')
	
finally:
	if result != 0:
		print('Host Down!!!')

'''
# -------

import os
from ping3 import ping


Host = input('Enter ip: ')
pac = input('Enter Number of packets: ')
result = os.system(f'ping -c {pac} {Host}')

print('')
if result == 0:
	print('Host Up!!!')
	
else:
	print('Host Down!!!')


x = ping(Host)
# Returns delay in seconds.
print(f'Delay Time: {x}s')



