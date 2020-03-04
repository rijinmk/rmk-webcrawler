import BeautifulSoup 
import time 
import random 
import urllib 
import os
import sys
import urlparse

if(len(sys.argv) > 1):
    print "Validating URL:", sys.argv[1]

    o = urlparse.urlparse(sys.argv[1])
    print o

else: 
    print "Please provide a URL"