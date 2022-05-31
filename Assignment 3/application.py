import datalayer as dl
import ticket_management as tm
import helper as helper


class App:
    # List tickets
    @staticmethod
    def list_tickets():
        # Get ticket objects list
        tickets = tm.Ticket.get_tickets()

        if tickets is not None:
            # Print the list in a friendly way
            for ticket in tickets:
                print('\n-----ID : ' + str(ticket.ID) + '----')
                ticket.print_ticket()
                print('------------\n')

            input('Press any key to continue...')
        else:
            input('No tickets found. Press any key to continue')

    # List ticket using a specific ID
    @staticmethod
    def list_ticket():
        ticket_id = input('Enter the ticket ID : ')
        
        ticket = None

        if tm.Ticket.validate_ticket_user_input(0, ticket_id):
            ticket = tm.Ticket.get_ticket(ticket_id)

        if ticket is not None:
            print('\n-----ID : ' + str(ticket.ID) + '----')
            ticket.print_ticket()
            print('-------------------')
            input('Press any key to continue...')
        else:
            input('Ticket ' + str(ticket_id) + ' not found! Press any key to continue...')

    # Add ticket.
    # It takes user input and does a basic validation.
    # It sends call to business layer and passes on the call to database.
    @staticmethod
    def add_ticket():
        while True:
            new_ticket = tm.Ticket()

            # Get title
            title = input('Enter ticket title : ')

            if tm.Ticket.validate_ticket_user_input(" ", title):
                new_ticket.title = title
            else:
                App.show_user_input_error('Title')

            # Get description
            description = input('Enter ticket description : ')

            if tm.Ticket.validate_ticket_user_input(" ", description):
                new_ticket.description = description
            else:
                App.show_user_input_error('Description')

            # Print list of options for priority
            helper.print_enums(tm.Priority)

            # Get and validate priority
            priority = input('Enter ticket priority number from above : ')

            if tm.Ticket.validate_ticket_user_input(tm.Priority.NO_PRIORITY, priority):
                new_ticket.priority = priority
            else:
                App.show_user_input_error('Priority')

            # Show list of users for selection
            helper.print_enums(tm.Users)

            # Get and validate "Added by user id"
            added_by_user_id = input('Enter ticket "Added by user ID" from above : ')

            if tm.Ticket.validate_ticket_user_input(tm.Users.NO_USER, added_by_user_id):
                new_ticket.added_by_user_id = added_by_user_id
            else:
                App.show_user_input_error('Added by user id')

            # Get and validate "Assigned to"
            helper.print_enums(tm.Users)

            assigned_to_user_id = input('Enter ticket "Assigned to user ID" from above : ')

            if tm.Ticket.validate_ticket_user_input(tm.Users.NO_USER, assigned_to_user_id):
                new_ticket.assigned_to_user_id = assigned_to_user_id
            else:
                App.show_user_input_error('Assigned to user id')

            new_ticket.status = 0  # Status is new for a new ticket

            new_ticket.add()

            print('New ticket has been added with ID ' + str(new_ticket.ID))
            input('Press any key to continue...')

    # Update ticket
    # This method firstly takes the input as ticket ID for the ticket to be updated
    # It show the current values for the ticket before asking updated values
    # Then it asks for new value for each attribute of the class. Press ENTER to skip to next field.
    # Each entry is validated for string and int
    @staticmethod
    def update_ticket():
        ticket_id = input('Enter ticket ID of the ticket to update')

        if tm.Ticket.validate_ticket_user_input(0, ticket_id):

            this_ticket = tm.Ticket.get_ticket(ticket_id)

            if this_ticket is None:
                input('Ticket not found! Press any key to continue...')
            else:
                print("\nCurrent values for ticket ID : " + str(ticket_id) + "\n")
                this_ticket.print_ticket()

                this_ticket_dict = helper.dict_from_class(this_ticket)

                for (attribute, value) in this_ticket_dict.items():
                    if attribute != 'ID':
                        new_value = input('\nEnter new value for ' + helper.get_friendly_attribute_name(attribute)
                                          + ' as "' + helper.get_friendly_type_name(str(type(value))) + '"'
                                          + tm.Ticket.get_enum_options_for_ticket_attribute(
                            attribute) + ' or press ENTER for the next ticket field.\n')

                        if new_value != "":
                            if tm.Ticket.validate_ticket_user_input(value, new_value):
                                this_ticket_dict[attribute] = new_value
                            else:
                                App.show_user_input_error(helper.get_friendly_attribute_name(attribute))

                input('Press any key to continue updating...')

                # Send a call to BL save this dictionary ticket
                tm.Ticket.save_as_dict(this_ticket_dict)

                new_ticket = tm.Ticket.get_ticket(ticket_id)

                print("\nUpdate values for ticket ID : " + str(ticket_id) + "\n")
                new_ticket.print_ticket()
                input('Press any key to continue...')
        else:
            input('\nERROR : Wrong input! Press any key to continue...\n')

    # Delete ticket CLI function
    @staticmethod
    def delete_ticket():
        ticket_id = input('Enter ticket ID to delete : ')

        this_ticket = None

        if tm.Ticket.validate_ticket_user_input(0, ticket_id):
            this_ticket = tm.Ticket.get_ticket(ticket_id)

        if this_ticket is None:
            input('Ticket not found! Press any key to continue...')
        else:
            tm.Ticket.delete(ticket_id)
            input('Ticket deleted. Press any key to continue...')

    # Hande user input error
    @staticmethod
    def show_user_input_error(input_name):
        input('Your input for "' + str(input_name) + '" is wrong. Press any key to restart...')
        App.start_command_line()

    # Command line main menu
    @staticmethod
    def start_command_line():
        while True:
            print('\n')
            print('##########-----------ITTMS Command Line-------------##########')
            user_selection_cli = input('Please press 0-6 to select an option from below : '
                                       + '\n 0 - Exit the CLI '
                                       + '\n 1 - Setup new database'
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
                App.list_tickets()
            elif user_selection_cli == '3':
                App.list_ticket()
            elif user_selection_cli == '4':
                App.add_ticket()
            elif user_selection_cli == '5':
                App.update_ticket()
            elif user_selection_cli == '6':
                App.delete_ticket()
            else:
                print('Wrong input!')
                continue


if __name__ == "__main__":
    while True:
        App.start_command_line()
