#!/usr/bin/env python
# This script update DNS server and pihole and ubiquiti controller in raspbian white!!!!!!
import paramiko
import time


devices = {'RaspDNS': {'ip': '11.0.0.254', 'username': 'pi', 'password': '@labi8621'},
           'UAP': {'ip': '11.0.0.108', 'username': 'pi', 'password': 'labi8621'}, }


commands = ('sudo apt update && sudo apt upgrade -y; pihole -up')

for device in devices.keys():
    print('-' * 25)
    print('Connection to {}: '.format(devices[device]['ip']))

    print('-' * 25)
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect(devices[device]['ip'], username=devices[device]
                ['username'], password=devices[device]['password'])
    stdin, stdout, stderr = ssh.exec_command(commands)
    stdin1, stdout1, stderr1 = ssh.exec_command('hostname')
    output1 = stdout1.readlines()
    output = stdout.readlines()
    print('Hostname: ', ''.join(output1))
    print(''.join(output))
    #print(' '.join(map(str, output)))
    time.sleep(1)
ssh.close()
