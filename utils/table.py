
class Seat:
    '''docstring'''
    def __init__(self):
        '''docstring'''
        self.free = True
        self.occupant = "empty"

    def set_occupant(self,name):
        '''docstring'''
        if self.free is True:
            self.occupant = name
            self.free = False

    def remove_occupant(self):
        '''docstring'''
        if self.free is False:
            self.free= True
            previousname = self.occupant
            self.occupant = "empty"
        return previousname


class Table:
    '''docstring'''

    def __init__(self, capacity):
        '''docstring'''
        self.capacity = capacity
        self.seats = []
        for i in range(capacity):
            #self.assets.append(Asset(asset_nam, asset_id,
            self.seats.append(Seat())


    def has_free_spot(self):
        '''docstring'''
        if self.left_capacity() > 0:
            return True
        else:
            return False




    def assign_seat(self, name):
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























