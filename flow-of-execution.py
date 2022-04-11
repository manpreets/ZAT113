

def print_twice(input_text):
    print_lines(input_text)
    print_lines(input_text)


def print_lines(input_text):
    print(input_text)


print_twice("Spam " * 4)
