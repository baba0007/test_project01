from pprint import pprint
import socket

information = socket.getaddrinfo('sahab.net', 'www')
info = information[0]
# info2 = information[10]
info3 = information[0:4]
pprint(info)
# pprint(info2)
pprint(info3)
