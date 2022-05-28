def find_longest_word(filename):
    '''Takes a filename and returns the longest word found in the file'''
    with open(filename) as f:
        content = f.read()
        words_dict = {word: len(word) for word in content.split()}
    return max(words_dict, key=words_dict.get)
import os

def find_all_longest_words(directory):
    '''Takes a directory and returns a dict in which the keys are the filenames 
    and the values are the longest words from each file'''
    longest_words = {filename: find_longest_word(os.path.join(directory, filename))
                                for filename in os.listdir(directory)
                                if os.path.isfile(os.path.join(directory, filename))}
    return longest_words

if __name__ == "__main__":
    print(find_all_longest_words('books'))
