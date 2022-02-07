import os
import time

#cwd = os.getcwd() #to know the current working directory
#print(cwd)

with open('ip-source.txt', 'r') as f:
    res = f.read()
    res = res.splitlines()
    print(res)

for ip in res:
    print('-'*40)
    os.system('clear') #will clear screen if you use the script from terminal
    print(f'pinging now {ip} :')
    print('')
    os.system(f'ping -c 2 {ip}')
    time.sleep(2)
    
