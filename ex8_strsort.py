def strsort(my_str):
    '''Take a string as an input and return a string with characters of the
    original string sorted from the lowest Unicode value to the highest Unicode
    value'''
    return ''.join(sorted(my_str))

if __name__ == "__main__":
    print(strsort('bca'))
