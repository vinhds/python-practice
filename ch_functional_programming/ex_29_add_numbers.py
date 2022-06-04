def sum_numbers(my_str):
    '''Takes a string as an argument, turn them into numbers and then sum them,
    ignores strings that can't be turned into integers. 
    Example: '10 abc 20 de44 30 55fg 40' will return 100.'''
    numbers_list = [int(ele) for ele  in my_str.split() if ele.isdigit()]
    return sum(numbers_list)

if __name__ == "__main__":
    user_input = input('Please enter a string:')
    print(sum_numbers(user_input))
