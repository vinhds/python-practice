def plword(word):
    result = ''
    if word[0] in 'aeiou':
        result = word + 'way'
    else:
        result = word[1:] + word[0] + 'ay'
    return result

def plfile(file_name):
    '''Takes a filename and returns a string with the file's contents but with
    each word translated into Pig Latin. 
    The returned translation ignores newlines and does not handloe capitalization 
    and punctuation in any specific way.
    Pig latin translation of a word:
    1. If the word begins with a vowel, add way to the end of the word.
    2. If the word begins with any other letter, take the first letter,
    put it on the end of the word and add ay.'''
    with open(file_name) as f:
        return ' '.join([plword(word) for line in f for word in line.split()])

if __name__ == "__main__":
    print(plfile('wcfile.txt'))
