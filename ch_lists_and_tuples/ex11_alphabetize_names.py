PEOPLE = [{'first': 'Reuven', 'last':'Lerner', 'email':'reuven@lerner.co.il'},
          {'first': 'Steve', 'last':'Head', 'email':'steve.head@lonestar.edu'},
          {'first': 'Valerie', 'last':'Jones', 'email':'valerie.jones@lonestar.edu'}]
def alphabetize_names(my_list):
    '''Takes a list of dictionaries where each dictionary consists of 3 keys:
        'first', ''last', and 'email' and return the list of dictionaries
        sorted by last name and then by first name'''
    sorted_list_1 = sorted(my_list, key=lambda item: [item['last'],
                                                      item['first']])
    return sorted_list_1

if __name__ == "__main__":
    print(alphabetize_names(PEOPLE))
