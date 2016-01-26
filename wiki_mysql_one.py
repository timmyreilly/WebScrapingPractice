from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import pymysql
import re

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='password1', db='mysql', charset='utf8') 

cur = conn.cursor()
cur.execute("USE scraping") 

random.seed(datetime.datetime.now()) 

def store(title, content):
    cur.execute("INSERT INTO pages (title, content) VALUES (\"%s\",\"%s\")", (title, content)) 
    cur.connection.commit() 

def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org"+articleUrl) 
    bsObj = BeautifulSoup(html) 
    title = bsObj.find("h1").find("span").get_text()
    content = bsObj.find("div", {"id":"mw-content-text"}).find("p").get_text()
    store(title, content) 
    return bsObj.find("div", {"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$"))

links = getLinks("/wiki/Kevin_Bacon") 
try: 
    while len(links) > 0:
        newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
        print(newArticle)
finally:
    cur.close()
    conn.close() 