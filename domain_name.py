import socket
import os

'''
#get ip of a domain:
def get_ip_address(url):
    host = url
    res = socket.gethostbyname(host)
    return res
url = input('Enter url: ')
print(get_ip_address(url))

#or
#get ip of a domain:
ip = os.popen(f'host {url}')
res1 = str(ip.read())
#print(res1)
res2 = res1.splitlines()[0]
print(res2)

# get nmap result: port scan on a domain:

def get_nmap(res2):
    ip = os.popen(f'host {url}')
    res1 = str(ip.read())
    res2 = res1.splitlines()[0]
    return os.system(f'nmap -F {res2}')
print(get_nmap(res2))
'''
#------------------------------------------------------------

print('-' * 40)
# or for nmap result from an ip:


def get_nmap(option, ip):
    command = 'nmap ' + option + ' ' + ip
    process = os.popen(command)
    result = str(process.read())
    return result


url = input('Enter url: ')
ip = socket.gethostbyname(url)
x = get_nmap('-F ', ip)
print('')
# print(f'Nmap Result for {url}: ')
print('Nmap Result for {}: '.format(url))
print('-' * 40)
print(x)

# saving nmap result to a file:
with open('domain-result.txt', 'w') as f:
    # f.write(f'Nmap Result for {url}: ' + '\n\n')
    f.write('Nmap Result for {}: '.format(url) + '\n\n')
    print('-' * 40)
    f.write(x)
f.close()
