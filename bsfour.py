from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page1.html")
bsObj = BeautifulSoup(html.read())
print(bsObj.h1) 


try: 
    html = urlopen("http://www.pythonscraping.com/pages/page1.html")
except: HTTPError as e:
    print(e)
    # return null, break, or go for plan b
else: 
    print("nice") 

    # program continues 
    # if you return or break in the exception catch you do not need to use the else statement 

if html is None: 
    print("URL is not found")
else: 
    # program continues
    print('nice') 

print(bsObj.nonExistentTag) 

try: 
    badContent = bsObj.nonExistentTag.anotherTag
except AttributeError as e: 
    print("tag was not found")
else: 
    print('nice') 
    if badContent == None:
        print("tag was not found")
    else:
        print("badContent")



