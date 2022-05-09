# Manpreet Singh | Student id - 632027 | Programming Task 7
from datetime import datetime
import Birthdays


# Pass level.

def run_pass_level():
    print('######-------Pass level----------######')
    today = datetime.now()
    print('Today\'s date : ' + today.strftime('%d %B %Y'))


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


# Distinction level main function
def run_distinction_level():
    print('######-------Distinction level-----------#######')
    Birthdays.get_birthdays()


# HD level main function
def run_hd_level():
    print('######-------HD level----------#####')
    # Add code to find the value of the 'July' key in the famousBirthdays dictionary and print the value to screen.
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
