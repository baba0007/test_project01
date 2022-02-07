#!/usr/bin/env python3.9

import netmiko
import json  # json = java script object notation

Edgeos = {'ip': '11.0.0.1',
          'device_type': 'vyos',
          'username': 'ubnt',
          'password': 'labi8621'}

uapos = {'ip': '11.0.0.100',
         'device_type': 'vyos',
         'username': 'baba007',
         'password': '@Labi8621'}

devices = [Edgeos, uapos]

exceptions = ()  # put all erros inside as tuple
for host in devices:
    try:
        print('Connection to {}'.format(host['ip']))
        connect = netmiko.ConnectHandler(**host)

        commands = ['date', 'ping -c 3 4.2.2.2']
        output = connect.send_config_set(commands)

    except exceptions as e:
        print('Failed to ', host['ip'], e)

    print(output)
    print('-' * 30)
connect.disconnect()
print()
print('End of the Script!!!', '*' * 20 + '*' * 20)
