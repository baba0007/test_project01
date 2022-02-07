'''
mail = input('Enter mail id: ')
try:
    i = mail.index('@')
    print('This mail contain @ symbol.')
    print(f'@ is at index: {i}')

except ValueError:
    print('This mail doe\'not contain @ symbol!')
'''
# --------------------------------------------------------
'''
alphabets = []
for i in range(65, 91):
    alphabets.append(chr(i))
print(alphabets)
for x in alphabets:
    print(x, end=' ')
print('')
'''
# -------------------------------------------------------

# smallest and largest number in a list:
'''
s = [2, 5, 10, 15, 90]
s.sort()

print('The smallest number is: ', s[0])
print(f'The biggest number is: {s[-1]}')
'''
# -------------------------------------------------------------
'''
import calendar, datetime
yy = 2020
mm = 10
x = calendar.month(yy, mm)
print(x)

now = datetime.datetime.now()
print(now)
'''
# ===============================================
'''
import calendar
for name in calendar.month_name:
    print(name)
print('-'*40)
for days in calendar.day_name:
    print(days)
'''
# -------------------------------------------------
'''
#count number of positive number and negative number in a list:
#l=[10,-21,4,-45,66,-93,1]
l=eval(input('Enter list :'))
count_pos=0
count_neg=0
for num in l:
    if num >= 0:
        count_pos += 1
    else:
        count_neg +=1
print(f'Numbers positive in the list are : {count_pos}')
print(f'Numbers negative in the list are : {count_neg}')
'''
# ---------------------------------------
'''
for e in os.uname():
    print(e)
'''
# ----------------------
'''
import platform
x = platform.uname()
print(x)
'''
# --------------------------------
'''
import os
ip = input('Enter ip : ')
res = ip.split('.')
print(res)
part0 = res[0]
part1 = res[1]
part2 = res[2]
part3 = res[3]
print('-'*40)
print('IP Range : ')
print('-'*40)
with open('ip-range1.txt', 'w') as f:
    for x in range(1,11):
        parts = part0 + '.' + part1 + '.' + part2 + '.' + str(x)
        print(parts)
        f.write(parts + '\n')
with open('ip-range1.txt', 'r') as f:
    res =f.read()
    res = res.splitlines()
    print(res)
    for ch in res:
        os.system(f'ping -c 2 {ch}')

f.close()
'''
# -----------------------------------
'''
import hashlib

text = 'hello'
text = text.encode('utf-8')
print(text)
hash_hash = hashlib.new('sha1') #u can choose md5 , sha1 and more
hash_hash.update(text)
print(hash_hash.hexdigest())
print(hash_hash.digest_size)
print(hash_hash.block_size)
'''
# ---------
'''
a = format(192, 'b') # convert decimal to binary ('b'=binary) ('X', hexadecimal upper case) ('x' hexadecimal lower case) ....
print(a)
'''
# --------------

# we need cisco device , will not work with Mikrotik , use paramiko for Mikrotik
'''
import netmiko
# for x in dir(netmiko):
#    print(x)
connection = netmiko.ConnectHandler(ip='11.0.0.1', device_type='cisco_os', username = 'admin', password = 'labi')
print(dir(connection))
'''
# ------------------------------
'''
import socket
hostname = input('Enter Domaine: ')
res = socket.gethostbyname(hostname)
print(f'{hostname} has an IP Address: {res}')
'''
# --------------------------
