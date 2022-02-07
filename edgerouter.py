from netmiko import ConnectHandler

edge = {
    'username': 'ubnt',
    'ip': '11.0.0.1',
    'verbose': True,
    'port': 22,
    'password': 'labi8621',
    'device_type': 'vyos'
}

net_connect = ConnectHandler(**edge)


commands = ['run show interfaces', 'run show arp', 'run show system image']

output = net_connect.send_config_set(commands)
print(output)
