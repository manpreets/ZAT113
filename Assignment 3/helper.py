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
