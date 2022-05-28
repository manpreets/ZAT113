from enum import Enum
import helper


class Priority(Enum):
    NO_PRIORITY = 0
    HIGH = 1
    MEDIUM = 2
    LOW = 3

    # Enum to handle priority
    @staticmethod
    def get_name():
        return 'I am Priority'


class TicketTest:
    priority: Priority

    def __init__(self, title, priority):
        self.title = title
        self.priority = Priority.NO_PRIORITY


this_ticket = TicketTest('Ticket 1', 0)

attributes = helper.dict_from_class(this_ticket)

for (key, value) in attributes.items():
    print('Key - ' + key + ' | Value - ' + str(value) + ' | Type __name__ - ' + type(value).__name__ + ' | Type as string : ' + str(type(value)))
