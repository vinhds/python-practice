def how_many_different_numbers(num_list):
    '''Takes a list of integers and returns the number of different integers it
    contains'''
    count_dict = {}
    for ele in num_list:
        count_dict[ele] = count_dict.get(ele, 0) + 1
    return len(count_dict.keys()) 

print(how_many_different_numbers([1,2,3,1,2,3,4,1]))

