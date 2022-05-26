# Class vehicle.

class Vehicle:
    def __init__(self, make='', year=0):
        self.make = make
        self.year = year

    def print_me(self):
        print('This vehicle "' + self.make + '" was made in ' + str(self.year))


class Car(Vehicle):
    def __init__(self, make='', year=0, model=''):
        super().__init__(make, year)
        self.model = model

    def print_me(self):
        print('This car "' + self.make + '" model - "' + self.model + '" was made in ' + str(self.year))


car_obj = Vehicle()
