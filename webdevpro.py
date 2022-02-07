#https://www.youtube.com/playlist?list=PLfyXUgjpxUVEP4vrZNcBV060t-8UFmIPa
#https://www.youtube.com/watch?v=xgp_Qc8NQX4&list=PLfyXUgjpxUVEP4vrZNcBV060t-8UFmIPa&index=1
#split ip in four parts:
'''
ip = '192.168.100.1'
res = ip.split('.')
print(res)
#print('.'.join(res))
for ch in res:
    print(ch)
res1 = [ch for ch in res]
print(res1)
'''
print('-'*40)

#create an ip list from 1 to 256 , only the last number varies:
import os
from time import sleep

ip = input('Enter ip addr: ')
res = ip.split('.')

part0 = res[0]
part1 = res[1]
part2 = res[2]
part3 = res[3]

print('')
f = open('ip-range.txt', 'w')
print('IP Range : ')
for x in range(1,4):
    parts = part0 + '.' + part1 + '.' + part2 + '.' + str(x)
    print(parts)
    f.write(parts + '\n')
print('-'*40)
with open('ip-range.txt', 'r') as f:
    for ip in f:
        os.system(f'ping -c 2 {ip}')
        sleep(1)
f.close()










