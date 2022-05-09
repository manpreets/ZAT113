# Manpreet Singh | Student id - 632027 | Programming Task 5
print('#############-----------Manpreet Singh | Student id - 632027 | Programming Task 5-----------###########')

# Pass level
print('######-------Pass level--------#######')

# Ask the user to input three random numbers between 1 and 10.
# Adapt your code when taking the inputs to ensure that the inputs are numbers. If they are not, store 0 instead.
import numpy


def get_variable_between_0_10(variable_name):
    v = 0
    # Loop runs until a right input is entered.
    while True:
        v = input('Please enter a random value for "' + variable_name + '" between 1 and 10 : ')
        # If input is not a number, then return 0.
        # Distinction level
        if not v.isdigit():
            v = 0
            break
        else:
            v = int(v)
            # Right input between 1 and 10
            if 1 <= v <= 10:
                break
            else:
                print('Wrong input for "' + variable_name + '"')

    print('-----------Final input for "' + variable_name + '" is : ' + str(v))
    return v


# Take these three random numbers and store them in variables.
variable_1 = get_variable_between_0_10('First variable')
variable_2 = get_variable_between_0_10('Second variable')
variable_3 = get_variable_between_0_10('Third variable')

# Credit level
print('######-------Credit level--------#######')


# Using Python (not a text editor) create a file called randomNumbers.txt and append each number to that file.
file_random_numbers = open('randomNumbers.txt', 'w')
file_random_numbers.writelines(str(variable_1) + '\n')
file_random_numbers.writelines(str(variable_2) + '\n')
file_random_numbers.writelines(str(variable_3) + '\n')
file_random_numbers.close()

file_random_numbers = open('randomNumbers.txt', 'r')
print(file_random_numbers.read())
file_random_numbers.close()

# HD level
print('######-------HD level--------#######')

# Ask the user to input another three random numbers between 1 and 10, with same input control from distinction level.
variable_4 = get_variable_between_0_10('Fourth variable')
variable_5 = get_variable_between_0_10('Fifth variable')
variable_6 = get_variable_between_0_10('Sixth variable')

# Store the numbers provided in a numpy two-dimensional array, with the first set in the first line and the second set
# in the second. Print the array.
variable_array = numpy.array([[variable_1, variable_2, variable_3],[variable_4, variable_5, variable_6]])
print(variable_array)

