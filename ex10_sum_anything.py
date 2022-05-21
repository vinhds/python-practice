def mysum(*args):
    '''Takes any number of arguments of the same type and add them up'''
    s = args[0]
    for i in range(1,len(args)):
        s += args[i]
    return s

if __name__ == "__main__":
    print(f"Sum of 'abc' and 'def' is {mysum('abc','def')}")
    print(f"Sum of [1,2,3] and[4,5,6] is {mysum([1,2,3],[4,5,6])}")
    print(f"Sum of 1,2,3 is {mysum(1,2,3)}")
    
