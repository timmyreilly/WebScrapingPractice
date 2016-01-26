from urllib.request import urlopen
textPage = urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1.txt")
print(textPage.read())

russianTextPage = urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt")
#print(russianTextPage.read())
print(str(russianTextPage.read(), 'utf-8'))