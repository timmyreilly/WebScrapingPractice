from nltk import word_tokenize
from nltk import Text 
from nltk.book import * 
from nltk import ngrams 

tokens = word_tokenize("Here is some not very interesting text") 
text = Text(tokens) 

fourgrams = ngrams(text6, 4) 
for fourgram in fourgrams:
    if fourgram[0] == "coconut":
        print(fourgram) 

