import tkinter as tk
import datalayer as dl
import ticket_management as tm
import helper as helper


# https://stackoverflow.com/questions/17466561/best-way-to-structure-a-tkinter-application


class Menubar(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

    def create_menu(self):
        button_create_ticket = tk.Button(self, text="Create ticket")
        button_list_tickets = tk.Button(self, text="List tickets")

        button_create_ticket.grid(column=0, row=0, padx=20, pady=10)
        button_list_tickets.grid(column=1, row=0, padx=20, pady=10)


class Statusbar(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.status_label = tk.Label(self)

    def set_status(self, label_text):
        self.status_label['text'] = label_text
        self.status_label.pack()


class Main(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent


class Application(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.parent = parent

        # Set up the title label of the application.
        main_title = tk.Label(self, text="Ticket Management System", font=("Arial", 25))
        main_title.pack(side="top", fill="x", pady=24)

        # Set up the menu bar.
        self.menubar = Menubar(self, highlightbackground="black", highlightthickness=1)

        # Set up the main frame.
        self.main = Main(self, borderwidth=2)

        # Set up the status bar
        self.statusbar = Statusbar(self, borderwidth=2, highlightthickness=1, highlightbackground="black")

        self.statusbar.set_status("I am the status label")

        # Set up the menu bar.
        self.menubar.create_menu()

        self.menubar.pack(side="top", fill="x")
        self.main.pack(side="top", fill="both", expand=True)
        self.statusbar.pack(side="bottom", fill="x")


# List tickets
def list_tickets():
    tickets = tm.Ticket.get_tickets()

    for ticket in tickets:
        print('\n-----ID : ' + str(ticket.ID) + '----')
        ticket.print_ticket()
        print('------------\n')


# List ticket using a specific ID
def list_ticket():
    ticket_id = input('Enter the ticket ID : ')
    ticket = tm.Ticket.get_ticket(ticket_id)
    print('\n-----ID : ' + str(ticket.ID) + '----')
    ticket.print_ticket()
    print('------------\n')


# Add ticket
def add_ticket():
    while True:
        new_ticket = tm.Ticket()
        new_ticket.title = input('Enter ticket title : ')
        new_ticket.description = input('Enter ticket description : ')
        helper.print_enums(tm.Priority)
        new_ticket.priority = input('Enter ticket priority number from above : ')
        helper.print_enums(tm.Users)
        new_ticket.added_by_user_id = input('Enter ticket added by ID from above : ')

        new_ticket.add()

        print('New ticket has been added with ID ' + str(new_ticket.ID))

        break


def get_friendly_attribute_name(attrib):
    attrib = attrib.replace('_', ' ').title()
    return attrib


def get_friendly_type_name(value_type):
    if value_type.find('str') > -1:
        return 'text'
    elif value_type.find('int') > -1:
        return 'number'


# Update ticket
def update_ticket():
    ticket_id = input('Enter ticket ID to update')

    if tm.Ticket.validate_ticket_user_input('id', ticket_id):

        this_ticket = tm.Ticket.get_ticket(ticket_id)

        print("\nCurrent values for ticket ID : " + str(ticket_id) + "\n")
        this_ticket.print_ticket()

        this_ticket_dict = helper.dict_from_class(this_ticket)

        for (attribute, value) in this_ticket_dict.items():
            if attribute != 'ID':
                new_value = input('Enter new value for ' + get_friendly_attribute_name(attribute)
                + ' as "' + get_friendly_type_name(str(type(value))) + '"'
                + tm.Ticket.get_enum_options_for_ticket_attribute(attribute) + ' or press ENTER for the next ticket field.\n')

                if tm.Ticket.validate_ticket_user_input(attribute, new_value):
                    this_ticket_dict[attribute] = new_value

        input('Press any key to continue updating...')

        tm.Ticket.save_as_dict(this_ticket_dict)

        new_ticket = tm.Ticket.get_ticket(ticket_id)

        print("\nUpdate values for ticket ID : " + str(ticket_id) + "\n")
        new_ticket.print_ticket()
    else:
        print('\nERROR : Wrong input\n')





# Delete ticket
def delete_ticket():
    ticket_id = input('Enter ticket ID to delete : ')
    tm.Ticket.delete(ticket_id)


def start_gui():
    root = tk.Tk()
    root.geometry('800x600')
    Application(root).pack(side="top", fill="both", expand=True)
    root.mainloop()


def start_command_line():
    while True:
        print('\n')
        print('##########-----------ITTMS Command Line-------------##########')
        user_selection_cli = input('Please press 0, 1 or 2 to select an option from below : '
                                   + '\n 0 - Exit the CLI '
                                   + '\n 1 - Setup database'
                                   + '\n 2 - List tickets'
                                   + '\n 3 - List ticket using ticket id'
                                   + '\n 4 - Add ticket '
                                   + '\n 5 - Update ticket '
                                   + '\n 6 - Delete ticket '
                                   )

        if user_selection_cli == '0':
            break
        elif user_selection_cli == '1':
            dl.setup_database()
        elif user_selection_cli == '2':
            list_tickets()
        elif user_selection_cli == '3':
            list_ticket()
        elif user_selection_cli == '4':
            add_ticket()
        elif user_selection_cli == '5':
            update_ticket()
        elif user_selection_cli == '6':
            delete_ticket()
        else:
            print('Wrong input!')
            continue


if __name__ == "__main__":
    while True:
        print('\n')
        print('##########-----------IT Ticket Management-------------##########')
        user_selection = input('Please press 0, 1 or 2 to select an option from below : '
                               + '\n 0 - Exit the program '
                               + '\n 1 - Start GUI'
                               + '\n 2 - Start command line '
                               )

        if user_selection == '0':
            break
        elif user_selection == '1':
            start_gui()
        elif user_selection == '2':
            start_command_line()
        else:
            print('Wrong input!')
            continue
