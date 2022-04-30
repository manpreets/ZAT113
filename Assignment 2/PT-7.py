# Manpreet Singh | Student id - 632027 | Programming Task 7
from datetime import datetime


# Pass level.

def run_pass_level():
    today = datetime.now()
    print(today.strftime('%d %B %Y'))


# Credit level
def run_credit_level():
    print('Credit level')


# Credit level
def run_distinction_level():
    print('Distinction level')


# Credit level
def run_hd_level():
    print('HD level')


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
