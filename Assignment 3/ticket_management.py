"""
This class is the business layer of the application. It uses enums for fixed value fields. This function be moved DB
tables. The enum fields are also type indicated and there are getter methods to get user-friendly version of the value.
It passes all the database CRUD calls to datalayer and passes on data from datalayer to application layer.
It uses static methods were operation on self object is not possible.
"""
import datalayer as dl
from enum import Enum
import helper as helper
from typing import get_type_hints


# Enum to handle priority
class Priority(Enum):
    NO_PRIORITY = 0
    HIGH = 1
    MEDIUM = 2
    LOW = 3


# Status of the ticket
class Status(Enum):
    NEW = 0
    OPEN = 1
    READY_FOR_REVIEW = 2
    UNDER_REVIEW = 3
    RESOLVED = 4


# The list of pre-defined users. This should be handled using a DB table for a production solution.
# todo - Use database for storing user data
class Users(Enum):
    NO_USER = 0
    Jack = 1
    Michael = 2
    Manpreet = 3


# Ticket class encapsulates basic attributes and methods of a ticket. DB calls for CRUD are achieved
class Ticket:
    priority: Priority
    assigned_to_user_id: Users
    added_by_user_id: Users
    status: Status

    def __init__(self,
                 ticket_id=0,
                 title='',
                 description='',
                 priority=Priority.NO_PRIORITY,
                 assigned_to_user_id=Users.NO_USER,
                 added_by_user_id=Users.NO_USER,
                 status=Status.NEW):
        self.ID = ticket_id
        self.title = title
        self.description = description
        self.priority = priority
        self.assigned_to_user_id = assigned_to_user_id
        self.added_by_user_id = added_by_user_id
        self.status = status

    # Gets user-friendly version of status
    def get_status(self):
        return Status(self.status).name

    # Gets user-friendly version of priority
    def get_priority(self):
        return Priority(self.priority).name

    # Gets user-friendly version of username for ticket author
    def get_added_by(self):
        return Users(self.added_by_user_id).name

    # Gets user-friendly version of username for ticket assigned to
    def get_assigned_to(self):
        return Users(self.assigned_to_user_id).name

    # Print user-friendly version of the ticket
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

    # Sends INSERT call to datalayer
    def add(self):
        new_ticket_id = dl.add_ticket(helper.dict_from_class(self))
        self.ID = new_ticket_id

    # Sends UPDATE call to datalayer
    def save(self):
        dl.update_ticket(helper.dict_from_class(self))

    # Static version of UPDATE call that uses dictionary to store ticket attirbutes
    @staticmethod
    def save_as_dict(dictionary_obj):
        dl.update_ticket(dictionary_obj)

    # DELETE call to datalayer
    @staticmethod
    def delete(ticket_id):
        dl.delete_ticket(ticket_id)

    # Ticket Parser - Takes rows from SELECT operation from DB and parses into list of tickets.
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

    # Gets single ticket record from datalayer
    @staticmethod
    def get_ticket(ticket_id):
        this_ticket_db = dl.get_ticket(ticket_id)

        tickets = Ticket.get_ticket_from_db_reader(this_ticket_db)

        if len(tickets) >= 1:
            return tickets[0]
        else:
            return None

    # Gets a list of all tickets
    @staticmethod
    def get_tickets():
        tickets_from_db = dl.get_tickets()

        # Ticket exists then return it otherwise return empty list

        tickets = None

        # Check the list of ticket got items
        if len(tickets_from_db) >= 1:
            tickets = Ticket.get_ticket_from_db_reader(tickets_from_db)

        return tickets

    # Returns a user-friendly list of enums in a form of key - value pair.
    # todo - Refactor this method to take take attribute as type and list's its members dynamically
    @staticmethod
    def get_enum_options_for_ticket_attribute(attribute):
        # Get types of all the attributes in Ticket class
        type_hints_for_ticket = get_type_hints(Ticket)

        prefix = ' from the following choices \n'

        # First the attribute should be one of enum or class and not a built-in type
        if attribute in type_hints_for_ticket.keys():
            # Attribute contains 'Priority' then get a list of its member
            if str(type_hints_for_ticket[attribute]).find('Priority') > -1:
                return prefix + helper.get_enums_as_friendly_list(Priority)
            # Attribute contains 'Users' then get a list of its member
            elif str(type_hints_for_ticket[attribute]).find('Users') > -1:
                return prefix + helper.get_enums_as_friendly_list(Users)
            # Attribute contains 'Status' then get a list of its member
            elif str(type_hints_for_ticket[attribute]).find('Status') > -1:
                return prefix + helper.get_enums_as_friendly_list(Status)
        else:
            return ''

    # Basic validation for str and int
    # todo - Advanced validation to check if input for enum based values belong to enum members
    @staticmethod
    def validate_ticket_user_input(attribute, value,   new_value):
        is_valid = False

        # Handles string members and check they are not empty after trimming from both sides
        if attribute == 'title' or attribute == 'description':
            is_valid = isinstance(value, str) and len(value.strip()) > 0
        # Handles int and enum based members
        elif attribute == 'priority' \
                or attribute == 'id' \
                or attribute == 'added_by_user_id' \
                or attribute == 'assigned_to_user_id' \
                or attribute == 'status':

            try:
                if helper.validate():
                    converted_value = int(value)
            except:
                is_valid = False

        return is_valid
