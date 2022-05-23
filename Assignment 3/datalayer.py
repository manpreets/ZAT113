import sqlite3
from TicketManagement import Ticket
from typing import Type


class DataLayer:
    def __init__(self):
        self.cursor = None
        self.conn = None
        self.database_file = None

    def __init__(self, database_file_name):
        self.cursor = None
        self.conn = None
        self.database_file = database_file_name

    # Connect to the database
    def connect(self):
        self.conn = sqlite3.connect(self.database_file)

        self.cursor = self.conn.cursor()

    def commit(self):
        self.conn.commit()
        self.conn.close()

    def close(self):
        self.conn.close


# Global datalayer variable
database = DataLayer('ITTMS.db')


# First time setup of the database
def setup_database():
    database.connect()
    database.conn.execute("""
        CREATE TABLE IF NOT EXISTS Tickets(
            Title text,
            Description text,
            Priority integer,
            Assigned_To_User_Id integer,
            Added_By_Staff_Id integer,
            Status integer 
        )
    """)
    database.commit()


# Add ticket

# Select tickets
def get_tickets():
    database.connect()
    database.cursor.execute("""
        SELECT *, oid FROM Tickets
    """)
    records = database.cursor.fetchall()
    database.commit()
    return records


# Select a ticket by id
def get_ticket(ticket_id):
    database.connect()
    database.cursor.execute("SELECT *, oid FROM Tickets WHERE oid =" + ticket_id)
    record = database.cursor.fetchall()
    database.commit()
    return record


# Update ticket
def update_ticket(ticket: Type[Ticket]):
    database.connect()
    database.cursor.execute("""
        UPDATE Tickets SET
        Title = :title,
        Description = :description,
        Priority = :priority,
        Assigned_To_User_Id = :assigned_to_user_id,
        Added_By_Staff_Id = :added_by_staff_id,
        Status = :status
        WHERE oid = :oid, 
        {
        'title' : ticket.title,
        'description' : ticket.description,
        'priority' : ticket.priority,
        'assigned_to_user_id' : ticket.assigned_to_user_id,
        'added_by_staff_id' : ticket.added_by_staff_id,
        'status' : ticket.status,
        'oid' : ticket.ID
        }
        
    """)
    records = database.cursor.fetchall()
    database.commit()
    return records
