def print_enums(the_enum):
    for item in the_enum:
        print(str(item.value) + ' - ' + item.name)

#https://jfine-python-classes.readthedocs.io/en/latest/dict_from_class.html
def dict_from_class(cls):
    return dict(
        (key, value)
        for (key, value) in cls.__dict__.items()
        if not key.startswith('__') and not callable(key)
    )
