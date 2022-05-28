# Write a mysum function that take a variable number of arguments and return
# the sum of them
def mysum(*args):
    s = 0
    for ele in args:
        s += ele
    return s

print(mysum(1,2,3))


# Write a function that takes two arguments: a list and an optional starting
# point and return the sum of the numbers in the list and the starting point

def mysum_2(num_list, starting_val=0):
    s = starting_val
    for ele in num_list:
        s += ele
    return s

print(mysum_2([1,2,3],4))

# Write a function that takes a list of numbers and return the average of those
# numbers
def myaverage(num_list):
    return mysum_2(num_list) / len(num_list)

print(myaverage([1,2,3]))

# Write a function that takes a list of words and return a tuple containing
# three integers: the length of the shortest word, the length of the longest
# word and the average word length

def word_stats(word_list):
    len_list = list(map(len, word_list))
    return min(len_list), max(len_list), myaverage(len_list)

print(word_stats(['abc','cdef','gj','a']))

# Write a function that takes a list of Python objects. Sum the objects that
# either are integers or can be turned into integers, ignoring the others.

def myspecialsum(object_list):
    s = 0
    for ele in object_list:
        try:
            x = int(ele)
            s += x
        except ValueError:
            pass
    return s

print(myspecialsum(['a','1',2,3.15,'cde','3.75']))
