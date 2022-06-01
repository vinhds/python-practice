def myxml(*args, **kargs):
    '''Creates XML output. The output will be a string.
    Examples: myxml('foo') --> <foo></foo>
    myxml('foo', 'bar') --> <foo>bar</foo>
    myxml('foo', 'bar', a=1, b=2, c=3) --> <foo, a="1", b="2", c="3">bar</foo>'''
    s = ''
    s += '<' + args[0]
    for key, value in kargs.items():
        s += ' ' + key + '=' + '"' + str(value) + '"'
    s += '>' 
    for i in range(1, len(args)):
        s += args[i]
    s += '</' + args[0] + '>'
    return s

if __name__ == "__main__":
    print(myxml('foo'))
    print(myxml('foo', 'bar'))
    print(myxml('foo', 'bar', a=1, b=2, c=3))


