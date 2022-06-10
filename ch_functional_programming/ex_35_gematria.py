# Create a dict whose keys are the lower case letters of the English alphabet
# and whose values are the numbers ranging from 1 to 26

import string
gematria_dict = {key:value for (key, value) in zip(string.ascii_lowercase, range(1,27))}

def gematria_for(word):
    '''Takes a single word and returns the gematria score for that word'''
    s = 0
    for char in word.lower():
        s += gematria_dict.get(char, 0)
    return s

dict_words = [word.strip() for word in open('words.txt')]

def gematria_equal_words(user_word):
    '''Takes a word and returns a list of those dict words whose gematria scores
    match the current word's score'''
    return [word for word in dict_words if gematria_for(word) == gematria_for(user_word)]

if __name__ == "__main__":
    print(gematria_equal_words('cat'))


