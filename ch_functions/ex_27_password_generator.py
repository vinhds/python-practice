import random
def create_password_generator(pass_chars):
    '''Takes a string and return a function which itself takes an integer argument.
    Calling this function will return a password of the specified length, using the string
    from which it was created.'''
    def passwd_gen(k):
        return ''.join(random.choices(pass_chars, k=k))
    return passwd_gen
  
if __name__ == "__main__":
    alpha_password = create_password_generator('abcdef')
    print(alpha_password(5))
    print(alpha_password(10))
    symbol_password = create_password_generator('!@#$%')
    print(symbol_password(5))
    print(symbol_password(10))

