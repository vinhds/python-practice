def get_final_line(filename):
    '''Takes a filename and return the file's final line on the screen'''
    my_list = []
    with open(filename) as f:
        my_list = list(f)
    return my_list[-1]

if __name__ == "__main__":
    print(get_final_line('file.txt'))

