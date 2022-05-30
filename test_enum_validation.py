from enum import Enum
import helper


class Color(Enum):
    red = 1
    blue = 2

input_var = 'dfas'

if helper.validate_enum(Color, input_var):
    print('Everything is fine and dandy.')
else:
    print('Everything is NOT fine and dandy.')
