# Manpreet Singh | Student id - 632027 | Programming Task 7

giftList = ['a book', 'chocolates', 'movie ticket', 'a surprise']

famousBirthdays = {'January': 'Mozart',
                   'February': 'Charles Darwin',
                   'March': 'Albert Einstein',
                   'April': 'Elizabeth II',
                   'May': 'Linnaeus',
                   'June': 'Josephine Baker',
                   'July': 'Frida Kahlo',
                   'August': 'Barack Obama',
                   'September': 'Elizabeth I',
                   'October': 'Gandhi',
                   'November': 'Marie Curie',
                   'December': 'Emily Dickinson'}


def get_birthdays():
    for birthday in famousBirthdays:
        print(birthday + ' - ' + famousBirthdays[birthday])
