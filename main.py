import pandas as pd
from utils.openspace import Openspace

df = pd.read_excel('bouman_8.xlsx', header = None)
names = df[0].tolist()


def get_num_of_tables():
    num_of_tables = int(input('Please enter the number of tables in the room: '))
    check(names, num_of_tables)

def check(names, num_of_tables):
    '''
    Checks if there are enough seats available for the list of givens names.
    If True, it calls the funcions that will organize the names.
    If False, it asks the user if they would like to add additional tables 
    before proceeding to organize the names.

    Parameters
    names - srt: namses in the list created from the given file.
    num_of_tables - int: total number of tables in the room
    '''

    table_capacity = 4 # Fixed table capacity
    if len(names) > num_of_tables * table_capacity:  
        print("Not enough seats for all people. ")
        reply = input('Do you want to add more tables? Yes (Y) / No (N)?    ')
        if reply == 'y' or reply == 'Y':
            get_num_of_tables()

        else:
            print('Okay! Have a nice day')
    else:
        op= Openspace(num_of_tables)
        op.organize(names)
        op.display()
        op.store()
        empty_spaces = (num_of_tables * 4) - len(names)
        print(f'There are {empty_spaces} seats left.')

get_num_of_tables()

