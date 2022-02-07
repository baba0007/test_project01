from domain_name import *
from whois import *

def gather_info(url):
    whois_1 = get_whois(url)
    domain_name = get_nmap('-F ', ip)
    

print(gather_info(url))
