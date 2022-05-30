from enum import Enum


# Prints an enum name and value pairs in a user-friendly way
def print_enums(the_enum):
    for item in the_enum:
        print(str(item.value) + ' - ' + item.name)


# Returns enum name and value as string
def get_enums_as_friendly_list(the_enum):
    return_string = ''

    for item in the_enum:
        return_string += str(item.value) + ' - ' + item.name + '\n'

    return return_string


# Prints a dictionary object in user friendly way
def print_dictionary(dictionary_obj):
    print(dictionary_obj)

    for (key, value) in dictionary_obj.items():
        print(key + ' - ' + str(value))


# The method was sourced from below site and modified to exclude callable items
# https://jfine-python-classes.readthedocs.io/en/latest/dict_from_class.html
def dict_from_class(cls):
    return dict(
        (key, value)
        for (key, value) in cls.__dict__.items()
        if not key.startswith('__') and not callable(key)
    )


# Validate enum for a user input
def validate_enum(the_enum, the_value):
    try:
        is_valid = issubclass(the_enum, Enum)
        # Convert into int and on exception return false

        the_value_int = int(the_value)

        # Check if the value is in the list of values in the enum
        is_valid = the_value_int in [item.value for item in the_enum]

        return is_valid
    except:
        return False


# Get a user friendly name for the class attribute name.
def get_friendly_attribute_name(attrib):
    attrib = attrib.replace('_', ' ').title()
    return attrib


# Get user friendly name for the attribute type.
# 'str' >> 'text'
# 'int' >> 'number'
def get_friendly_type_name(value_type):
    if value_type.find('str') > -1:
        return 'text'
    elif value_type.find('int') > -1:
        return 'number'
