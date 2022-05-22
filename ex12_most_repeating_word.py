from collections import Counter

def most_repeating_character(word):
    return Counter(word).most_common(1)[0][1]
def most_repeating_word(word_list):
    '''Takes a list of string and return the string that contains the greatest
    number of repeated letters'''

    my_list = [most_repeating_character(word) for word in word_list]
    location = my_list.index(max(my_list))
    return word_list[location]

if __name__ == "__main__":
    words = ['this', 'is', 'an', 'elementary', 'test', 'example']
    print(f"The most repeating word is {most_repeating_word(words)}")

