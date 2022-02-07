import socket
from geoip import geolite2

hostname = input('Enter Domaine: ')
ipaddr = socket.gethostbyname(hostname)
print(f'{hostname} IP Address : {ipaddr}')
match = geolite2.lookup(ipaddr)
if match is not None:
    #print(match.country)
    print('Country: ',match.country)
    print('Continent: ',match.continent)
    print('Time zone: ', match.timezone)
    print('Location: ', match.location)    
