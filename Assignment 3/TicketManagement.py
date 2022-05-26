import datalayer as dl
from enum import Enum
import Helper as helper


class Priority(Enum):
    HIGH = 1
    MEDIUM = 2
    LOW = 3


class Status(Enum):
    NEW = 1
    OPEN = 2
    READY_FOR_REVIEW = 3
    UNDER_REVIEW = 4
    RESOLVED = 5


class Users(Enum):
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

    def add(self):
        new_ticket_id = dl.add_ticket(helper.dict_from_class(self))
        self.ID = new_ticket_id

    def save(self):
        dl.update_ticket(helper.dict_from_class(self))

    @staticmethod
    def get_ticket(ticket_id):
        ticket_from_db = dl.get_ticket(ticket_id)

        # todo Null check
        # if ticket exists then return it otherwise return null
        this_ticket = Ticket(
            ticket_from_db[0],
            ticket_from_db[1],
            ticket_from_db[2],
            ticket_from_db[3],
            ticket_from_db[4],
            ticket_from_db[5],
            ticket_from_db[6],
        )

        return this_ticket

    @staticmethod
    def get_tickets():
        tickets_from_db = dl.get_tickets()

        # todo Null check
        # if ticket exists then return it otherwise return empty list

        tickets = []

        for ticket in tickets_from_db:
            this_ticket = Ticket(
                this_ticket[0],
                this_ticket[1],
                this_ticket[2],
                this_ticket[3],
                this_ticket[4],
                this_ticket[5],
                this_ticket[6]
            )

        return tickets
