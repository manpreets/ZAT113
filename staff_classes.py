from datetime import datetime as d

class Person:
    def __init__(self, first_name, last_name, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        # Parse date
        _dob = d.strptime(date_of_birth, '%d/%m/%Y')
        self.date_of_birth = _dob

    def get_details(self):
        return 'First name : ' + self.first_name + \
               '\n' + 'Last name : ' + self.last_name + \
               '\n' + 'Date of birth : ' + d.strftime(self.date_of_birth, '%d/%m/%Y')

    def full_name(self):
        return self.first_name + ' ' + self.last_name

    def print_me(self):
        print(self.get_details())

    # Write to file. Append only
    def write_to_file(self, file_name):
        file_to_write = open(file_name, 'a')
        file_to_write.write(self.get_details())
        file_to_write.close()


class Staff(Person):
    def __init__(self, first_name, last_name, date_of_birth, department):
        super().__init__(first_name, last_name, date_of_birth)
        self.department = department

    def get_details(self):
        return super().get_details() + \
               '\n' + 'Department : ' + self.department

    def print_me(self):
        print(self.get_details())


def run_pass_level():
    # A person named Jon Snow, who was born on the 18 July 1990 and works in the accounts department
    staff1 = Staff('Jon', 'Snow', '18/07/1998', 'Accounts Department')

    # Jon Snow printed to screen
    print(staff1.full_name())
    staff1.print_me()


run_pass_level()
