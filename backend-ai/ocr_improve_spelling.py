from fuzzywuzzy import fuzz
from fuzzywuzzy import process

def get_closest_words(input_word, word_list, threshold=80, top_n=3):
    
    matches = process.extractOne(input_word, word_list, scorer=fuzz.ratio)
    
    return matches[0]


#input_word = "Frvg;( 2"  
#input_word = input_word.lower()
#word_list = ["fragile", "flammable", "toxic", "password", "pass", "passport", "past", "word", "ward"]

#Find best match
#print(get_closest_words(input_word, word_list))
