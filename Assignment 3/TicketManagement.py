import datalayer as dl
from enum import Enum
import Helper as helper
from typing import get_type_hints


class Priority(Enum):
    NO_PRIORITY = 0
    HIGH = 1
    MEDIUM = 2
    LOW = 3


class Status(Enum):
    NEW = 0
    OPEN = 1
    READY_FOR_REVIEW = 2
    UNDER_REVIEW = 3
    RESOLVED = 4


class Users(Enum):
    NO_USER = 0
    Jack = 1
    Michael = 2
    Manpreet = 3


class Ticket:
    priority: Priority
    assigned_to_user_id: Users
    added_by_user_id: Users

    def __init__(self,
                 ticket_id=0,
                 title='',
                 description='',
                 priority=Priority.NO_PRIORITY,
                 assigned_to_user_id=Users.NO_USER,
                 added_by_user_id=Users.NO_USER,
                 status=0):
        self.ID = ticket_id
        self.title = title
        self.description = description
        self.priority = priority
        self.assigned_to_user_id = assigned_to_user_id
        self.added_by_user_id = added_by_user_id
        self.status = status

    def get_status(self):
        return Status(self.status).name

    def get_priority(self):
        return Priority(self.priority).name

    def get_added_by(self):
        return Users(self.added_by_user_id).name

    def get_assigned_to(self):
        return Users(self.assigned_to_user_id).name

    def add(self):
        new_ticket_id = dl.add_ticket(helper.dict_from_class(self))
        self.ID = new_ticket_id

    def save(self):
        dl.update_ticket(helper.dict_from_class(self))

    def print_ticket(self):
        print(
            'ID : ' + str(self.ID) + '\n'
                                     'Title : ' + self.title + '\n'
                                                               'Description : ' + self.description + '\n'
                                                                                                     'Priority : ' + self.get_priority() + '\n'
                                                                                                                                           'Added by : ' + self.get_added_by() + '\n'
                                                                                                                                                                                 'Assigned to : ' + self.get_assigned_to() + '\n'
                                                                                                                                                                                                                             'Status : ' + self.get_status() + '\n'
        )

    @staticmethod
    def save_as_dict(dictionary_obj):
        dl.update_ticket(dictionary_obj)

    @staticmethod
    def delete(ticket_id):
        dl.d

    @staticmethod
    def get_ticket_from_db_reader(ticket_db_reader):
        tickets = []

        for this_ticket_db in ticket_db_reader:
            temp_ticket = Ticket(
                this_ticket_db[0],  # ID
                this_ticket_db[1],  # Title
                this_ticket_db[2],  # Description
                this_ticket_db[3],  # Priority
                this_ticket_db[4],  # Assigned to
                this_ticket_db[5],  # Added by
                this_ticket_db[6]  # Status
            )

            tickets.append(temp_ticket)

        return tickets

    @staticmethod
    def get_ticket(ticket_id):
        this_ticket_db = dl.get_ticket(ticket_id)

        tickets = Ticket.get_ticket_from_db_reader(this_ticket_db)

        if len(tickets) == 1:
            return tickets[0]
        else:
            return None

    @staticmethod
    def get_tickets():
        tickets_from_db = dl.get_tickets()

        # todo Null check
        # if ticket exists then return it otherwise return empty list

        tickets = Ticket.get_ticket_from_db_reader(tickets_from_db)

        return tickets

    @staticmethod
    def get_enum_options_for_ticket_attribute(attribute):
        type_hints_for_ticket = get_type_hints(Ticket)

        prefix = ' from the following choices \n'

        if attribute in type_hints_for_ticket.keys():
            if str(type_hints_for_ticket[attribute]).find('Priority') > -1:
                return prefix + helper.get_enums_as_friendly_list(Priority)
            elif str(type_hints_for_ticket[attribute]).find('Users') > -1:
                return prefix + helper.get_enums_as_friendly_list(Users)
        else:
            return ''

    @staticmethod
    def validate_user_input(attribute, value):
        is_valid = False

        if attribute == 'title' or attribute == 'description':
            is_valid = isinstance(value, str) and len(value) > 0
        elif attribute == 'priority' or attribute == 'id' or attribute == 'added_by_user_id' or attribute == 'assigned_to_user_id' or attribute == 'status':

            try:
                converted_value = int(value)
                is_valid = isinstance(converted_value, int)
            except:
                is_valid = False

        return is_valid
