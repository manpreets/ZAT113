# Manpreet Singh | Student id - 632027 | Programming Task 8
import tkinter as tk
# Pass level.
pt9_window = tk.Tk()
# Pass level main function
def run_pass_level():
    pt9_window.title('ZAT113 Task 9')


# Credit level

# Credit level main function
def run_credit_level():


# Distinction level

# Distinction level main function
def run_distinction_level():


# HD level

# HD level main function
def run_hd_level():

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
