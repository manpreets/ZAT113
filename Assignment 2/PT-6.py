# Manpreet Singh | Student id - 632027 | Programming Task 6
from datetime import datetime as d
from pathlib import Path

print('#############-----------Manpreet Singh | Student id - 632027 | Programming Task 6-----------###########')

# Pass level
print('######-------Pass level--------#######')


# A class which creates a generic staff member. Staff members have a date of birth ‘dd/mm/yyyy’, first name,
# last name, and department
class Person:
    def __init__(self, first_name, last_name, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        # Parse date
        _dob = d.strptime(date_of_birth, '%d/%m/%Y')
        self.date_of_birth = _dob

    def get_details(self):
        return '\n        First name : ' + self.first_name + \
               '\n        Last name : ' + self.last_name + \
               '\n        Date of birth : ' + d.strftime(self.date_of_birth, '%d/%m/%Y')

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
               '\n        Department : ' + self.department

    def print_me(self):
        print(self.get_details())


def run_pass_level():
    # A person named Jon Snow, who was born on the 18 July 1990 and works in the accounts department
    staff1 = Staff('Jon', 'Snow', '18/07/1998', 'Accounts Department')

    # Jon Snow printed to screen
    print('\n         Full name : ' + staff1.full_name() + '\n')
    staff1.print_me()


# Credit level
# A class which creates a generic staff member, allowing for initialisation on entry, but otherwise the same as
# the pass-level requirements above
# --------Created above
print('######-------Credit level--------#######')


# A prompt that allows the user to enter a staff member’s details to create a new staff object
def create_staff_from_user_input():
    while True:
        first_name = input('        Enter the first name of the staff : ')
        last_name = input('        Enter the last name of the staff : ')
        date_of_birth = input('        Enter the date of birth of the staff in dd/mm/yyyy format : ')
        department = input('        Enter the department name of the staff : ')

        try:
            staff_object = Staff(first_name, last_name, date_of_birth, department)
            return staff_object
        except:
            input('        Input error. Press any key to continue...')
            continue

        break


def run_credit_level():
    staff_2 = create_staff_from_user_input()
    # The staff member details printed to screen on completion of entry.
    staff_2.print_me()


# Distinction level
# A class which creates a teaching staff member, which inherits the basic staff attributes from the class created in the
# credit-level, but also includes discipline and license number attributes
class TeachingStaff(Staff):
    def __init__(self, first_name, last_name, date_of_birth, department, discipline, license_number):
        super().__init__(first_name, last_name, date_of_birth, department)
        self.discipline = discipline
        self.license_number = license_number

    def get_details(self):
        return super().get_details() + \
               '\n' + '        Discipline : ' + self.discipline + \
               '\n' + '        Licence number : ' + self.license_number

    def print_me(self):
        print(self.get_details())


def create_teaching_staff_from_user_input():
    while True:
        user_input = input('        Do you want to add teaching staff? Press any key for yes and 0 for no :  ')

        if user_input == '0':
            break

        first_name = input('        Enter the first name of the teaching staff : ')
        last_name = input('        Enter the last name of the teaching staff : ')
        date_of_birth = input('        Enter the date of birth of the teaching staff in dd/mm/yyyy format : ')
        department = input('        Enter the department of the teaching staff : ')
        discipline = input('        Enter the discipline of the teaching staff : ')
        license_number = input('        Enter the license number of the teaching staff : ')

        try:
            teaching_staff_object = TeachingStaff(first_name, last_name, date_of_birth, department, discipline,
                                                  license_number)
            return teaching_staff_object
            break
        except:
            input('        Input error. Press any key to continue...')
            continue


# A prompt that allows the user to enter the teacher staff member’s details to create a new teaching staff object
def run_distinction_level():
    # A prompt that allows the user to enter a staff member’s details to create a new staff object
    teaching_staff_1 = create_teaching_staff_from_user_input()
    # The teaching staff member details printed to screen on completion of entry.
    teaching_staff_1.print_me()


# High Distinction Level
# As per distinction-level requirement above except:
#
# The program should operate in an endless loop (with 0 as an exit key) so that once staff details are entered,
# the user can enter details for the additional staff members.
# The user should get to choose whether they enter a staff member or a teaching staff member
# All staff members generated should be printed into a txt file.

# Start of endless loop
def create_staff_member(file_name):
    staff_member = create_staff_from_user_input()
    staff_member.print_me()
    staff_member.write_to_file(file_name)


def create_teaching_staff_member(file_name):
    teaching_staff_member = create_staff_from_user_input()
    teaching_staff_member.print_me()
    teaching_staff_member.write_to_file(file_name)


def print_staff_file(file_name):
    staff_file = open(file_name)
    # Check if file is created or otherwise create it
    file_path = Path(file_name)

    if file_path.is_file():
        print(staff_file.read())
    else:
        input('        File error. Press any key to continue...')


def run_hd_level():
    while True:
        print('\n\n')
        print('###########---------------Test HD Level - Main menu-------------########')
        user_selection = input('    Please press 0, 1 or 2 to select an option from below : '
                               + '\n    0 - Exit the HD level to Main Menu '
                               + '\n    1 - Create staff member '
                               + '\n    2 - Create teaching staff member '
                               + '\n    3 - Print the file '
                               )
        file_name = 'pt_6.txt'
        # Check if file is created or otherwise create it
        file_path = Path(file_name)

        if not file_path.is_file():
            new_file_to_write = open(file_name, 'x')
            new_file_to_write.close()

        if user_selection == '0':
            break
        elif user_selection == '1':
            create_staff_member(file_name)
        elif user_selection == '2':
            create_teaching_staff_member(file_name)
        elif user_selection == '3':
            print_staff_file(file_name)
        else:
            print('Wrong input!')
            continue


def main():
    while True:
        print('\n\n')
        print('##########-----------Programming Task 6 - Main menu-------------##########')
        user_selection = input('Please press 0, 1 or 2 to select an option from below : '
                               + '\n 0 - Exit the program '
                               + '\n 1 - Test Pass level'
                               + '\n 2 - Test Credit level '
                               + '\n 3 - Test Distinction '
                               + '\n 4 - Test HD Level '
                               )

        if user_selection == '0':
            break
        elif user_selection == '1':
            run_pass_level()
        elif user_selection == '2':
            run_credit_level()
        elif user_selection == '3':
            run_distinction_level()
        elif user_selection == '4':
            run_hd_level()
        else:
            print('Wrong input!')
            continue


# Run main function
main()
