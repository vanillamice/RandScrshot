from bs4 import BeautifulSoup
import urllib.parse
from urllib.request import urlopen,Request
import random
import string
import requests
import webbrowser

letters_and_digits = string.ascii_letters + string.digits
result_nmbr = ''.join((random.choice(string.ascii_lowercase) for i in range(2)))
result_ltr = ''.join((random.choice(string.digits) for i in range(4)))
result_str = result_nmbr + result_ltr
URLMAIN = "https://prnt.sc/"+result_str
#print (URLMAIN)


requester = {'User-Agent': 'Mozilla/5.0'}
req=Request(URLMAIN,headers=requester)
u =urlopen(req)


soup = BeautifulSoup(u.read(), features="lxml")



links = soup.find_all('a')

images =[]

for img in soup.findAll('img'):
    images.append(img.get('src'))
    
img=random.choice(images)
    
#print(img)

URLL = img
webbrowser.open(URLL, new=1)

