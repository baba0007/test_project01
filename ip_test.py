from ipaddress import IPv4Network

def get_network():
    ip = input('Enter Network: ')
    net = IPv4Network(ip)
    ip_range = net.num_addresses
    print(f'Prefix of the Network is : {net.prefixlen}')
    print(f'The Netmask is : {net.netmask}')
    print(f'The Network IP Address is : {net.network_address}')
    print(f'Broadcast IP Address : {net.broadcast_address}')
    print(f'Number of ip addresses is : {ip_range}')
    if ip_range >= 2:
        print(f'Number of usable IP Addresses is : {ip_range - 2}')
    else:
        print('Number of usable IP Addresses is : 0')
    print('-'*40)
    print('The Usable IP Addresses are: ')
    #print(list(net.hosts())[0])
    for y in list(net.hosts()):
                  print(y)
    
    print('-'*40)
    #for x in net:
     #   print(x)
        
get_network()
