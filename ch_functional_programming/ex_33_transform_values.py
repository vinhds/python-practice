def transform_values(func, a_dict):
    '''Takes a function and a dictionary and returns a new dictionary
    whose keys are the same as the input dictionary but whose values 
    have been transformed by the function func'''
    return {key: func(value) for key, value in a_dict.items()}    

if __name__ == "__main__":
    d = {'a':1, 'b':2, 'c':3}
    print(transform_values(lambda x:x*x, d))
