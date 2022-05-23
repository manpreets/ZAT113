import tkinter as tk
import TicketManagement


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


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('800x600')
    Application(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
