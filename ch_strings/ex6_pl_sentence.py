from ex5_pig_latin import pig_latin
def pl_sentence(my_str):
    word_list = my_str.split()
    new_list = [pig_latin(word) for word in word_list]
    return ' '.join(new_list)


if __name__ == "__main__":
    print(pl_sentence('this is a test translation'))
    
