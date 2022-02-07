import ipaddress
net = ipaddress.IPv4Network(input('Enter Network address: '))
count = 0
for addr in net:
    print(addr)
    count += 1
print(f'Number of ip address is : {count}')
ip = ipaddress.ip_address(input('Enter ip address: '))
print(f'{ip} is in {net} : {ip in net}')
