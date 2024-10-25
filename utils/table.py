class Seat:
    '''
    Class that defines a seat on the table,
    whether is free or who the occupant is.
    '''

    def __init__(self):
        '''
        Creates a Seat object.
        
        Atributes:
        Free - bool: Indicates if no occupant is on the seat.
        Occupant - str: name of the person the seat is assigned to
        '''

        self.free = True
        self.occupant = "empty"

    
    def __str__(self):
        return f'A seat on the table.'
    

    def set_occupant(self,name):
        '''
        Assigns a person to the seat and
        returns the name of the occupant.

    
        Parameters:
        names - str: list of names created from excel file.
        '''

        if self.free is True:
            self.occupant = name
            self.free = False

    def remove_occupant(self) -> str:
        '''
        Removes someone from a seat and returns
        the name of who the occupant was.

        Returns:
        previousname - str: name of the occupant the seat was assiged to before it was removed.
        '''

        if self.free is False:
            self.free= True
            previousname = self.occupant
            self.occupant = "empty"
        return previousname


class Table:
    '''
    Defines an table object with n number of Seat objects

    Attributes:
    Capacity - int: The number of seats on the table
    '''

    def __init__(self, capacity):

        '''
        Creates a Table object with n number of seats.
        '''

        self.capacity = capacity
        self.seats = []
        for i in range(capacity):
            #self.assets.append(Asset(asset_nam, asset_id,
            self.seats.append(Seat())


    def __str__(self):
        return f'A table with {self.capacity} seats.'


    def has_free_spot(self):
        '''
        Checks if the object has empty seats.

        Returns
        Bool: True or false depending on whethere the table has free seats 
        '''

        if self.left_capacity() > 0:
            return True
        else:
            return False


    def assign_seat(self, name):
        '''
        Assigns an occupant to a free seat on the table.

        Parameters:
        name = name from the input document, who becomes the occupant of the seat
        '''

        if self.has_free_spot() is True:
            for s in self.seats:
                if s.free is True:
                    s.set_occupant(name)
                    break

    def left_capacity(self):
        counter = 0
        for s in self.seats:
            if s.free is True:
                counter += 1
        return counter

    def print_everything(self):
        for s in self.seats:
            print(s.free)
            print(s.occupant)
        print (f"Left Capacities{self.left_capacity()}")
