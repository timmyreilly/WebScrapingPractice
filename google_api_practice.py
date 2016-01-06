from urllib.request import urlopen
from tokens import *
from pprint import * 

html = "https://maps.googleapis.com/maps/api/geocode/json?address=1+Science+Park+Boston+MS+02114&key=" + GOOGLE_API_KEY

raw = urlopen(html) 
