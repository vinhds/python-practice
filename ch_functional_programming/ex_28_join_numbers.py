def join_numbers(range_of_int):
    '''Takes a range of integers. Returns those numbers as a string, with commas 
    between the numbers.'''
    my_list = [str(i) for i in range_of_int]
    return ','.join(my_list)

if __name__ == "__main__":
    print(join_numbers(range(15)))
