import datalayer as dl
from enum import Enum
import Helper as helper


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
    def __init__(self, ticket_id=0, title='', description='', priority=0, assigned_to_user_id=0, added_by_user_id=0,
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
                this_ticket_db[6]   # Status
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

        if len(tickets) == 1:
            return tickets[0]
        else:
            return None


