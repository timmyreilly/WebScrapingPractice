from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html) 

nameList = bsObj.find_all("span", {"class":"green"})
nameAndDialogue = bsObj.find_all("span", {"class":{"green", "red"}})

for name in nameList:
    print(name.get_text())

for words in nameAndDialogue:
    print(words.get_text())

princeText = bsObj.findAll(text="the prince")
print(len(princeText))

allText = bsObj.findAll(id="text")
print(allText[0].get_text())