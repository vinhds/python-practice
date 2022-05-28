def dictdiff(dict_1, dict_2):
    '''Takes two dicts as arguments. Return a new dict that expresses the
    difference between the dicts.
    Rule: - If there are no differences between the dicts, returns an empty
    dict.
    - For each key-value pair that differs, the return value of dictdiff will
    have a key-value pair in which the value is a list containing the values
    from the two different dicts. If one of the dicts doesn't contain that key,
    it should contain None.'''
    result_dict = {}
    for key in dict_1.keys():
        if dict_1.get(key) != dict_2.get(key):
            result_dict[key] = [dict_1.get(key), dict_2.get(key)]
    for key in dict_2.keys():
        if key not in result_dict.keys() and dict_1.get(key) != dict_2.get(key): 
            result_dict[key] = [dict_1.get(key), dict_2.get(key)]
    return result_dict

d1 = {'a':1, 'b':2, 'c':3}
d2 = {'a':1, 'b':2, 'c':4}
d3 = {'a':1, 'b':2, 'd':3}
d4 = {'a':1, 'b':2, 'c':4}
d5 = {'a':1, 'b':2, 'd':4}
if __name__ == "__main__":
   print(dictdiff(d1,d2)) 
   print(dictdiff(d1,d1)) 
   print(dictdiff(d3,d4)) 
   print(dictdiff(d1,d5)) 
   
