


class Seat:
    """
    Class representing a single seat that can be occupied
    """

    def __init__(self)-> None:
        """
        Constructor for the Seat class.
        :tran if the seat is currently available
        :Store the number of the person occypying the seat
        """

        self.free: bool = True
        self.occupant: str = ""

    def __str__(self) -> str:
        """
        String representation of Seat instance.
        :return: A string stating the occupancy status of tha seat.
        """
        if self.free:
            return "Seat is free."
        return f"Seat is occupied by {self.occupant}."

    def set_occupant(self, name:str) -> bool:
        """
        Function that will assign occupant to the seat if it is free.
        :param name: A string representing the person to sit in the seat.
        :return: A bool indicating if the seat was successfully assigned
        """

        if self.free:
            self.occupant = name
            self.free = False
            return True
        return False

    def remove_occupant(self) ->optional:

        if not self.free:
            name = self.occupant
            self.occupant = ""
            self.free = True
            return name
        return None
    
    def __str__(self):
        pass



class Table:
    def __init__(self, capacity=4):
        self.capacity = capacity
        self.seats = [Seat() for _ in range(capacity)]

    def has_free_spot(self):

        return any(seat.free for seat in self.seats)

    def assign_seat(self, name):

        for seat in self.seats:
            if seat.free:
                seat.set_occupant(name)
                return True
        return False

    def left_capacity(self):

        return sum(seat.free for seat in self.seats)


