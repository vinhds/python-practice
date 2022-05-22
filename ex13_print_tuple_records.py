PEOPLE = [('Donald', 'Trump', 7.85), \
          ('Vladimir', 'Putin', 3.626),\
          ('Jinping', 'Xi', 10.603)]
def format_sort_records(tuples_list):
    '''Takes a list of tuple and returns a formatted string.
    Rule: - Each record is one line.
          - Each record has 3 fields: last name, first name and time.
          - The name fields has 10 characters, time has 5 characters with one
          space character of padding between each of the columns.
          - Time is rounded to two digits.'''
    s = "{:<10} {:<10} {:^10.2f}"
    for ele in tuples_list:
        print(s.format(ele[1], ele[0], ele[2]))
if __name__ == "__main__":
    format_sort_records(PEOPLE)
