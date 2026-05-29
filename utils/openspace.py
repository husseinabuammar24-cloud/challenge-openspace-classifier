# Your code here
import random
from utils.table import Table

class OpenSpace:
    def __init__(self, number_of_tables = 6):
        self.number_of_tables = number_of_tables
        self.tables = [Table(capacity = 4) for _ in range(self.number_of_tables)]

    def organize(self,names):
        shuffled_names = names.copy()
        random.shuffle(shuffled_names)

        for name in shuffled_names:
            for table in self.tables:
                if table.has_free_spot():
                    table.assign_seat(name)
                    break
    
    def display(self):
        print ("\n ***OpenSpace seating chart***")

        for index, table in enumerate (self.tables, 1):
            occupants = [seat.occupant for seat in table.seats if not seat.free] 

            if occupants:
                seats_str = ", ".join (occupants)
            else:
                seats_str = "Emptry Table"
                print(f"Table{index}, {seats_str}")
    

    def store (self, filename):
        with open(filename, "w") as file:
            file.write("-***OpenSpace Seating Chart***-\n\n")
            for index, table in enumerate(self.tables, 1):
                occupants = [seat.occupant for seat in table.seats if not seat.free]
                seats_str = ", ".join(occupants) if occupants else "Empty Table"
                file.write(f"Table {index}: {seats_str}\n")
        print (f"Seating chart successfully saved to '{filename}'")
