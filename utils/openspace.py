import random
import pandas as pd # type: ignore

class Openspace:
    """
    Defines a room in the office.
    """

    def __init__(self, tables, number_of_tables):
        self.tables = tables #Need to import table object from table.py
        self.number_of_tables = number_of_tables
    
    def __str__(self) ->str:
        return f'A room with {self.number_of_tables} tables of {self.tables}.'
    
    def organize(self, names):
        """
        Randomly assigns people to Seat objects in the table objects.
        """

        for table in self.tables:
            while table.has_free_spot():
                random_name = random.randint(0, len(names) - 1)
                table.set_occupant(names[random_name])
                names.remove(names[random_name])

    def display(self):
        """
        Displays the distribution of people per table
        """
        headers = []
        num = 1
        for table in self.tables:
            headers.append('Table ' + str(number))
            number += 1

        tables_df = pd.DataFrame(self.tables, columns=headers)
        print(tables_df)

    def store(self, filename):
        pass



###############################

students = [['cel', 'bea', 'leo' ], ['pilar', 'cata', 'dino'], ['flora', 'diego', 'jose']]
headers = []

number = 1
for group in students:
    headers.append('Table ' + str(number))
    number += 1


students_df = pd.DataFrame(students, columns=headers)
print(students_df)

