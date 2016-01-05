from urllib.request import urlopen
from bs4 import BeautifulSoup
import re 

html = urlopen("http://www.pythonscraping.com/pages/page3.html") 
bsObj = BeautifulSoup(html) 

twos = bsObj.findAll(lambda tag: len(tag.attrs) == 2) 
print(twos)