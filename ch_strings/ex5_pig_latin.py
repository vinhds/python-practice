def pig_latin(my_str):
    '''Translate a string to Pig Latin
    Rule: - If the word begins with a vowel, add way to the end of the word.
          - If the word begins with any other letter, take the first letter, 
          put it at the end of the word and add ay.'''
    new_str = ''
    if my_str[0] in 'aeiou':
        new_str = my_str + 'way'
    else:
        new_str = my_str[1:] + my_str[0] + 'ay'
    return new_str

if __name__ == "__main__":
    user_str = input('Please enter a string: ')
    print(f'{user_str} translated to Pig Latin: {pig_latin(user_str)}')
          

    
