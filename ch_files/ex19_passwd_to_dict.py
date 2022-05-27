def passwd_to_dict(filename):
    '''return a dict based on file passwd in which the dict's keys are usernames and the values are the users' IDs'''
    result_dict = {}
    with open(filename) as f:
        for line in f:
            if not((line.startswith('#')) or (line.startswith(' '))):
                line_list = line.split(':')
                result_dict[line_list[0]] = int(line_list[2])
    return result_dict

if __name__ == "__main__":
    print(passwd_to_dict('passwd.txt'))
