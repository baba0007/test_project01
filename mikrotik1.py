import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #to not use ssh key.
client.connect('11.0.0.1', username='admin', password='labi')
#stdin is a variable input to send commands
#stdout is a variable output to get result from the sent commands from sdtin.
#stderr is a variable to show you error if you get error.
#stdin, stdout, stderr = client.exec_command('ip address print')
#stdin1, stdout2, stderr2 = client.exec_command('interface print')
#stdin, stdout, stderr = client.exec_command('ip firewall connection print')
#stdin, stdout, stderr = client.exec_command('ip route p')
stdin, stdout, stderr = client.exec_command('sys package update check-for-updates') #to check system router update
#stdin, stdout, stderr = client.exec_command('sys package update install') #to install updates
#stdin, stdout, stderr = client.exec_command('sys routerboard print') #to check routerboard firmware version and info.
#stdin, stdout, stderr = client.exec_command('sys routerboard upgrade') #to upgrade routerboard firmware.

# print('IP Addresses :\n')
for line in stdout:
    print(line.strip('\n')) #to delete space lines.
    #print(line)
print('-'*80)
# print('Interfaces :\n')
# for line in stdout2:
    # print(line.strip('\n'))
client.close()

#if we wana see what inside the object client:
# for x in dir(client):
    # print(x)
    