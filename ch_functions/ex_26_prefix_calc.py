import operator
def calc(to_solve):
    '''Takes a string containing a simple math expression in prefix notation with an operator
    and two numbers, parses the input and produce the appropriate output. Assumes that the argument 
    will only contain one of the basic six operators and two valid numbers. 
    Implementation: Each of the operations is implemented as a separate function and use no if statement 
    to decide which function should be run.'''
    operations = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv,\
                    '**': operator.pow, '%': operator.mod}
    op, first_s, second_s = to_solve.split()
    first = int(first_s)
    second = int(second_s)
    return operations[op](first, second)

if __name__ == "__main__":
    print(calc('+ 2 3'))

