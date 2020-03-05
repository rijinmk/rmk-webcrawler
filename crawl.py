import BeautifulSoup 
import time 
import random 
import requests
import os
import sys
import urlparse
import validators

if(len(sys.argv) > 1):
    print "Validating URL:", sys.argv[1]

    if(validators.url(sys.argv[1])):
        url = sys.argv[1]
        # raw_html = requests.get(url, verify=True).text

        # https://stackoverflow.com/questions/23013220/max-retries-exceeded-with-url-in-requests
        page = ''
        while page == '':
            try:
                page = requests.get(url, verify=True)
                break
            except:
                print("Connection refused by the server..")
                print("Let me sleep for 5 seconds")
                print("ZZzzzz...")
                time.sleep(5)
                print("Was a nice sleep, now let me continue...")
                continue

        bs = BeautifulSoup.BeautifulSoup(page.text)
        links = bs.findAll('a') 
        print len(links)
        for i in links: 
            time.sleep(2)
            print i
            print
 
    else: 
        print "Please enter a valid URL"

else: 
    print "Please provide a URL"