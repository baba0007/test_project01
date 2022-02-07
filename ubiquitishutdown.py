import netmiko
import json  # json = java script object notation

Edgeos = {'ip': '11.0.0.1',
          'device_type': 'vyos',
          'username': 'ubnt',
          'password': 'labi8621'}


print('Connection to {}'.format(Edgeos['ip']))
connect = netmiko.ConnectHandler(**Edgeos)

#commands = ['date', 'ping -c 3 4.2.2.2']
commands = ['shutdown']
output = connect.send_config_set(commands)

print(output)
print('-' * 30)
connect.disconnect()
print()
print('End of the Script!!!', '*' * 20 + '*' * 20)
