class Seat():
    """
    Class that defines a seat on the table,
    whether is free or who the occupant is.
    """

    def __init__(self, free=True, occupant=''):
        self.free =  free
        self.occupant = occupant


    def set_occupant(self, name) -> str:
        """
        Assigns a person to the seat and
        returns the name of the occupant.
        """

        self.occupant = name
        self.free = False
        return self.occupant

    def remove_occupant(self) -> str:
        """
        Removes someone from a seat and returns
        the name of who the occupant was.
        """

        old_occupant = self.occupant
        self.occupant = ""
        self.free = True
        return old_occupant



name = 'Pilar'
name2 = 'Catalina'

silla = Seat()

silla.set_occupant(name)
print(silla.occupant)

silla.remove_occupant()
print(silla.occupant)

silla.set_occupant(name2)
print(silla.occupant)

silla.remove_occupant()
print(silla.occupant)

























