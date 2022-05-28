import csv
def passwd_to_csv(filename_1, filename_2):
    '''Takes two filenames. Reads from the passwd-style file and write the username (index 0)
    and user ID (index 2), separated by a tab character, in the output file'''
    with open(filename_1) as f1:
        with open(filename_2, 'w') as f2:
            o = csv.writer(f2, delimiter='\t')
            for line in f1:
                if not line.startswith(('#', '\n')):
                    user_info = line.split(':')
                    o.writerow([user_info[0], user_info[2]])

if __name__ == "__main__":
    passwd_to_csv('passwd.txt', 'passwd.csv')


