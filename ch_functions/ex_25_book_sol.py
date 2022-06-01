def myxml(tagname, content='', **kwargs):
    attrs = ''.join([f' {key}="{value}"' for key, value in kwargs.items()])
    return f'<{tagname}{attrs}>{content}</{tagname}>'

if __name__ == "__main__":
    print(myxml('foo'))
    print(myxml('foo', 'bar'))
    print(myxml('foo', 'bar', a=1, b=2, c=3))
    
