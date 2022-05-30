from enum import Enum


# Validate enum for a user input
def validate_enum(the_enum, the_value):
    is_valid = issubclass(the_enum, Enum)
    # Convert into int and on exception return false
    try:
        the_value_int = int(the_value)
    except:
        return is_valid

    # Check if the value is in the list of values in the enum
    is_valid = the_value_int in [item.value for item in the_enum]

    return is_valid



class Color(Enum):
    red = 1
    blue = 2

input_var = 'dfas'

if validate_enum(Color, input_var):
    print('Everything is fine and dandy.')
else:
    print('Everything is NOT fine and dandy.')
