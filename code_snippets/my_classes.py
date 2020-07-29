# The purpose of this code is to serve as a simple
# example of OOP in Python

class Flight():

    def __init__(self, capacity):
        # creating two new properties (capacity and passengers for the class)
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if self.open_seats():
            self.passengers.append(name)
            print(f"Seat booked for {name}")
        else:
            print(f"No available seats for passenger {name}")

    def open_seats(self):
        if self.capacity - len(self.passengers) > 0:
            return True
        else:
            return False

flight = Flight(3)
passengers = ["Walid", "Michal", "Mario"]

for passenger in passengers:
    flight.add_passenger(passenger)
