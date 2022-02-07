from rich import print, pretty, inspect
from paramiko import SSHClient, AutoAddPolicy
import time

host = '192.168.3.254'
port = '22'
username = 'pi'
password = '@labi8621'

ssh = SSHClient()
ssh.set_missing_host_key_policy(AutoAddPolicy())
ssh.connect(host, port, username, password)

if ssh.get_transport() is not None:
    print("Connected")
else:
    print("Not Connected")

# x = inspect(ssh, methods=True)  # will print what we can do with paramiko.SSHClient():
# print(x)

# cmds = '/sbin/ifconfig | grep inet'
cmds = 'sudo apt update && sudo apt upgrade -y && pihole -up && sudo apt clean && sudo apt autoclean && sudo apt autoremove'

stdin, stdout, stderr = ssh.exec_command(cmds)
time.sleep(2)

output = stdout.readlines()
output2 = stderr.readlines()
print(output)

# Get return code from command (0 is default for success):
x = stdout.channel.recv_exit_status()
print(f'Return Code: {x}')

if x == 0:
    print('Everything is Ok.')
else:
    print('Not Success.')
    print(output2)

print('')
# print(output2)

# Because they are file objects, they need to be closed:
stdin.close()
stdout.close()
stderr.close()

# Close the client itself:
ssh.close()
