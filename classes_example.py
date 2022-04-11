# Class vehicle.

class Vehicle:
    def __init__(self):
        self.make = ''
        self.year = 0

    def __init__(self, make, year):
        self.make = make
        self.year = year

    def print_me(self):
        print('This vehicle "' + self.make + '" was made in ' + str(self.year))


class Car(Vehicle):
    def __init__(self):
        super().__init__(self)

    def __init__(self, make, year, model):
        super().__init__(make, year)
        self.model = model

    def print_me(self):
        print('This car "' + self.make + '" model - "' + self.model + '" was made in ' + str(self.year))


car_obj = Vehicle('Ford', 2000)
car_obj.print_me()