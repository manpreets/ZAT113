# Manpreet Singh | Student id - 632027 | Programming Task 8
from datetime import datetime
import Birthdays


# Pass level.
def count_characters():
    string_input = input('Enter a string \n')
    print('Number of characters : ' + string_input.count())

def compare_strings():
    string_1 = input('Enter string 1 \n')
    string_2 = input('Enter string 2 \n')
    print('Are both string same : ' + string_1 == string_2)



def run_pass_level():
    print('######-------Welcome to pass level----------######')
    while True:
        user_selection_pass_level = input('Please press 0, 1 or 2 to select an option from below : '
                               + '\n If you want to exit the program, enter 0'
                               + '\n If you want to count the characters in a string, enter 1'
                               + '\n If you want to compare two strings, enter 2\n'
                               )
        if user_selection_pass_level == '0':
            break
        elif user_selection_pass_level == '1':
            count_characters()
        elif user_selection_pass_level == '2':
            compare_strings()
        else:
            print('Wrong input!')
            continue



def get_dob_from_user():
    dob_input = input('        Enter the date of birth of the user in dd/mm/yyyy format : ')
    return datetime.strptime(dob_input, '%d/%m/%Y')


# Credit level
def run_credit_level():
    print('######-------Credit level------------######')
    dob_datetime = get_dob_from_user()
    dob_formatted = dob_datetime.strftime('%d %B')
    print('Your birthday is on ' + dob_formatted)

    user_input = 0
    while True:
        try:
            user_input = int(input('Enter a digit between 0 and 3'))
            if 0 <= user_input <= 3:
                break
            else:
                show_wrong_input_message()
        except:
            show_wrong_input_message()
            continue

    print(Birthdays.giftList[user_input])


def show_wrong_input_message():
    print("You have not entered an integer between 0 and 3, try again")


# Credit level
def run_distinction_level():
    print('######-------Distinction level-----------#######')
    Birthdays.get_birthdays()


# Credit level
def run_hd_level():
    print('######-------HD level----------#####')
    print(Birthdays.famousBirthdays['July'])

    user_dob = get_dob_from_user()
    user_dob_month = user_dob.strftime('%B')

    print(Birthdays.famousBirthdays[user_dob_month] + ' was also born in ' + user_dob_month)


def main():
    while True:
        print('\n\n')
        print('##########-----------Programming Task 7 - Main menu-------------##########')
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