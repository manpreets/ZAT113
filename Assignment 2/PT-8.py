# Manpreet Singh | Student id - 632027 | Programming Task 8
print('#############-----------Manpreet Singh | Student id - 632027 | Programming Task 8-----------###########')

# Pass level.
# A function to display the number of characters in a string
def count_characters():
    string_input = input('Enter a string \n')
    print('Number of characters : ' + str(len(string_input)))


# A function to compare strings if both are the same
def compare_strings():
    string_1 = input('Enter string 1 \n')
    string_2 = input('Enter string 2 \n')
    print('Are both string same? : ' + str(string_1 == string_2))


# A generic function to loop through a list of strings and ask for a user input
def get_user_selection(options):
    for option in options:
        print(option)

    return input('Enter your selection from above : ')


# Pass level main function
def run_pass_level():
    while True:
        print('\n\n######-------Welcome to pass level----------######\n')

        options_list_pass = ['If you want to exit pass level to main menu, enter 0',
                             'If you want to count the characters in a string, enter 1',
                             'If you want to compare two strings, enter 2']
        # Gets user input for selection
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
# Converts a string to upper case
def convert_sting_uppercase():
    string_to_be_upper = input('Enter the string to be converted to upper : ')
    print(string_to_be_upper.upper())


# Converts a string to lowercase
def convert_sting_lowercase():
    string_to_be_lower = input('Enter the string to be converted to lower : ')
    print(string_to_be_lower.lower())


# Credit level main function
def run_credit_level():
    while True:
        print('\n\n######-------Welcome to Credit level------------######\n')
        options_list_credit = ['If you want to exit the credit level to main menu, enter 0',
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
# Compares two strings to find if one contains another
def compare_string_includes_other():
    string_1 = input('Enter string 1 : ')
    string_2 = input('Enter string 2 : ')

    # Find positions of a string in other, returns -1 if not found
    print('Does string 1 contains string 2? : ' + str(string_1.find(string_2) != -1))


# Concatenates two strings
def join_stings():
    string_1 = input('Enter string 1 : ')
    string_2 = input('Enter string 2 : ')

    print('Concatenated strings are :')
    print(string_1 + string_2)


# Distinction level main function
def run_distinction_level():
    while True:
        print('\n\n######-------Welcome to Distinction level------------######\n')
        options_list_distinction = ['If you want to exit the distinction level to main menu, enter 0',
                                    'If you want to count the characters in a string, enter 1',
                                    'If you want to compare two strings, enter 2',
                                    'If you want to change the string to uppercase, enter 3',
                                    'If you want to change the string to lowercase, enter 4',
                                    'If you want to compare two strings if one has the other, enter 5',
                                    'If you want to join two strings, enter 6']

        user_selection_distinction_level = get_user_selection(options_list_distinction)

        if user_selection_distinction_level == '0':
            break
        elif user_selection_distinction_level == '1':
            count_characters()
        elif user_selection_distinction_level == '2':
            compare_strings()
        elif user_selection_distinction_level == '3':
            convert_sting_uppercase()
        elif user_selection_distinction_level == '4':
            convert_sting_lowercase()
        elif user_selection_distinction_level == '5':
            compare_string_includes_other()
        elif user_selection_distinction_level == '6':
            join_stings()
        else:
            print('Wrong input!')
            continue


# HD level
# Counts the number of occurrences of a substring in a string
def count_a_character_in_string():
    string_1 = input('Enter a string : ')
    character_1 = input('Enter a character : ')

    print('Count of "' + character_1 + '" in the string is ' + str(string_1.count(character_1)))


# HD level main function
def run_hd_level():
    while True:
        print('\n\n######-------Welcome to HD level------------######\n')
        options_list_hd = ['If you want to exit the HD level to main menu, enter 0',
                           'If you want to count the characters in a string, enter 1',
                           'If you want to compare two strings, enter 2',
                           'If you want to change the string to uppercase, enter 3',
                           'If you want to change the string to lowercase, enter 4',
                           'If you want to compare two strings if one has the other, enter 5',
                           'If you want to join two strings, enter 6',
                           'If you want to count the number of times a character appears in a string, enter 7']

        user_selection_hd_level = get_user_selection(options_list_hd)

        if user_selection_hd_level == '0':
            break
        elif user_selection_hd_level == '1':
            count_characters()
        elif user_selection_hd_level == '2':
            compare_strings()
        elif user_selection_hd_level == '3':
            convert_sting_uppercase()
        elif user_selection_hd_level == '4':
            convert_sting_lowercase()
        elif user_selection_hd_level == '5':
            compare_string_includes_other()
        elif user_selection_hd_level == '6':
            join_stings()
        elif user_selection_hd_level == '7':
            count_a_character_in_string()
        else:
            print('Wrong input!')
            continue

# Main function
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
