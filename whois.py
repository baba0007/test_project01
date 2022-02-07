import os

def get_whois(url):
    command = 'whois ' + url
    process = os.popen(command)
    result = str(process.read())
    return result
url = input('Enter url: ')
print(get_whois(url))

