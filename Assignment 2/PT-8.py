# Manpreet Singh | Student id - 632027 | Programming Task 8
from datetime import datetime
import Birthdays


# Pass level.
def count_characters():
    string_input = input('Enter a string \n')
    print('Number of characters : ' + str(len(string_input)))


def compare_strings():
    string_1 = input('Enter string 1 \n')
    string_2 = input('Enter string 2 \n')
    print('Are both string same : ' + str(string_1 == string_2))


def get_user_selection(options):
    for option in options:
        print(option)

    return input('Enter your selection from above : ')


def run_pass_level():
    while True:
        print('\n\n######-------Welcome to pass level----------######')

        options_list_pass = ['If you want to exit the program, enter 0',
                             'If you want to count the characters in a string, enter 1',
                             'If you want to compare two strings, enter 2']

        user_selection_pass_level = get_user_selection(options_list_pass)

        if user_selection_pass_level == '0':
            break
        elif user_selection_pass_level == '1':
            count_characters()
        elif user_selection_pass_level == '2':
            compare_strings()
        else:
            print('Wrong input!')
            continue


# Credit level
def convert_sting_uppercase():
    string_to_be_upper = input('Enter the string to be converted to upper : ')
    print(string_to_be_upper.upper())


def convert_sting_lowercase():
    string_to_be_lower = input('Enter the string to be converted to upper : ')
    print(string_to_be_lower.lower())


def run_credit_level():
    while True:
        print('######-------Welcome to Credit level------------######')
        options_list_credit = ['If you want to exit the program, enter 0',
                               'If you want to count the characters in a string, enter 1',
                               'If you want to compare two strings, enter 2',
                               'If you want to change the string to uppercase, enter 3',
                               'If you want to change the string to lowercase, enter 4']

        user_selection_credit_level = get_user_selection(options_list_credit)

        if user_selection_credit_level == '0':
            break
        elif user_selection_credit_level == '1':
            count_characters()
        elif user_selection_credit_level == '2':
            compare_strings()
        elif user_selection_credit_level == '3':
            convert_sting_uppercase()
        elif user_selection_credit_level == '4':
            convert_sting_lowercase()
        else:
            print('Wrong input!')
            continue


# Distinction level
def run_distinction_level():
    while True:
        print('######-------Welcome to Distinction level------------######')
        options_list_credit = ['If you want to exit the program, enter 0',
                               'If you want to count the characters in a string, enter 1',
                               'If you want to compare two strings, enter 2',
                               'If you want to change the string to uppercase, enter 3',
                               'If you want to change the string to lowercase, enter 4']

        user_selection_credit_level = get_user_selection(options_list_credit)

        if user_selection_credit_level == '0':
            break
        elif user_selection_credit_level == '1':
            count_characters()
        elif user_selection_credit_level == '2':
            compare_strings()
        elif user_selection_credit_level == '3':
            convert_sting_uppercase()
        elif user_selection_credit_level == '4':
            convert_sting_lowercase()
        else:
            print('Wrong input!')
            continue


# Credit level
def run_hd_level():
    print('######-------Welcome to HD level----------#####')


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
