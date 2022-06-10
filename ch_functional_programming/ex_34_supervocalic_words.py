def get_sv(filename):
    '''Takes the name of a text file containing one word per line. Find all the words
    that are (almost) supervocalic, i.e., contain a, e, i, o and u and return a set 
    containing them'''
    with open(filename) as f:
        return {word.strip() for word in f if set('aeiou').issubset(set(word.lower()))}

if __name__ == "__main__":
    print(get_sv('words.txt'))
