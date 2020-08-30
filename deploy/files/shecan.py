#!/bin/python
## python web scraping script
### Automating Changing resolv config for docker installation
import requests
from bs4 import BeautifulSoup

# get ips from shecan DNS ip addresses
proxy={} # use proxy if needed
response = requests.get('https://shecan.ir' , proxies=proxy)
    #get html of the site
result = BeautifulSoup(response.text ,'html.parser' )
    #use Beautifull soup to read htmls
res = result.find_all('span' , attrs={'class':'shecan-dns-ips'}) 
for dns in res:
    DnsAddress = dns.text
        # pass output into bash command 
    f = open("/tmp/resolv.conf", "a+")
    f.write("nameserver"+" "+ DnsAddress + "\n")
    f.close()
    print("correct")
print("Done!")
