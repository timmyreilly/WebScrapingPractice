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

# [('Strange', 'NNP'), ('women', 'NNS'), ('lying', 'VBG'), ('in', 'IN'), ('ponds', 'NNS'), ('distributing', 'VBG'), ('swords', 'NNS'), ('is', 'VBZ'), ('no', 'DT'), ('basis', 'NN'), ('for', 'IN'), ('a', 'DT'), ('system', 'NN'), ('of', 'IN'), ('government', 'NN'), ('.', '.'), ('Supreme', 'NNP'), ('executive', 'NN'), ('power', 'NN'), ('derives', 'NNS'), ('from', 'IN'), ('a', 'DT'), ('mandate', 'NN'), ('from', 'IN'), ('the', 'DT'), ('masses', 'NNS'), (',', ','), ('not', 'RB'), ('from', 'IN'), ('some', 'DT'), ('farcical', 'JJ'), ('aquatic', 'JJ'), ('ceremony', 'NN'), ('.', '.')]

from nltk import pos_tag

text = word_tokenize("Strange women lying in ponds distributing swords is no bases for a system of government. Supreme executive power derives from a mandate from the masses, not from some farcical aquatic ceremony.") 

print(pos_tag(text)) 