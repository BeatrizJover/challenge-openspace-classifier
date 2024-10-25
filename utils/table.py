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
        self.capacity = capacity # #La capacidad de la mesa en asientos
        self.seats = []
        for i in range(capacity):
            self.seats.append(Seat()) #Aqui se crean objetos del Tipo Seat en la lista


    def has_free_spot(self): #Si capacidad restante es mayor de 0 dice que hay un asiento libre
        '''docstring'''
        if self.left_capacity() > 0:
            return True
        else:
            return False




    def assign_seat(self, name):
        if self.has_free_spot() is True:
            for s in self.seats:
                if s.free is True:
                    # Si la mesa tiene capacidad, se recorre la lista de asientos y en el primer asiento libre se pone un nombre
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
            print(s.occupant, end="\t\t")
        print (f"Empty Seats: {self.left_capacity()}")























