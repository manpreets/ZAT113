import datalayer as dl


class Ticket:
    def __init__(self):
        self.ID = 0
        self.title = ''
        self.description = ''
        self.priority = 0
        self.assigned_to_user_id = 0
        self.added_by_user_id = 0
        self.status = 0

    def __init__(self, ticket_id, title, description, priority, assigned_to_user_id, added_by_user_id, status):
        self.ID = ticket_id
        self.title = title
        self.description = description
        self.priority = priority
        self.assigned_to_user_id = assigned_to_user_id
        self.added_by_user_id = added_by_user_id
        self.status = status

    @staticmethod
    def get_ticket(ticket_id):
        ticket_from_db = dl.get_ticket()

        # if ticket exists then return it otherwise return null

    @staticmethod
    def get_tickets():
        tickets_from_db = dl.get_tickets()

        # if ticket exists then return it otherwise return null
