def ubbi_dubbi(my_str):
    '''Take a word and translate it to Ubbi Dubbi
    Rule: Every vowel is prefaced with ub'''
    new_str = ''
    for char in my_str:
        if char in 'aeiou':
            new_str = new_str + 'ub' + char
        else:
            new_str += char
    return new_str

if __name__ == "__main__":
    print(f'octobus translated to:  {ubbi_dubbi("octopus")}')
    print(f'elephant translated to:  {ubbi_dubbi("elephant")}')
    print(f'milk translated to:  {ubbi_dubbi("milk")}')
    print(f'program translated to:  {ubbi_dubbi("program")}')
