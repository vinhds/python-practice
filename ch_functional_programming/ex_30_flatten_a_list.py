def flatten(num_list):
    '''Takes a list of list (just one element deep) and returns a flat
    one-dim version of the list. Only flattens a two-level list
    Example: flatten([[1, 2], [3, 4]] --> [1, 2, 3, 4]'''
    return [ele for list_ele in num_list for ele in list_ele]


if __name__ == "__main__":
    print(flatten([[1, 2], [3, 4]]))

