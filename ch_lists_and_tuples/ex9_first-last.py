def firstlast(my_sequence):
    '''Takes a sequence (string, list, or tuple) and returns that first and
    last elements of that sequence in a two-element sequence of the same
    type'''
    l = len(my_sequence)
    return my_sequence[slice(0, l, l-1)]
if __name__ == "__main__":
    print(firstlast('abc'))
    print(firstlast([1,2,3,4]))
    print(firstlast((3,7,'a','d')))
