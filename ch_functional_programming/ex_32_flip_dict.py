def flip_dict(my_dict):
    '''Takes a dict of any size in which the keys are unique and the 
    values are also unique, turns the dict inside out such that keys
    and the values are reversed'''
    return {value: key for key, value in my_dict.items()}

if __name__ == "__main__":
    d = {'a':1, 'b': 2, 'c': 3}
    print(flip_dict(d))
