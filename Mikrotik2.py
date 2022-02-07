from librouteros import connect
import pprint

api = connect(username='admin', password='labi', host='11.0.0.1')
ip_info = api(cmd="/ip/address/print")

for item in ip_info:
    #print(item)
    pprint.pprint(item) #to print nicely
   