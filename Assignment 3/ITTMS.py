import tkinter as tk


# https://stackoverflow.com/questions/17466561/best-way-to-structure-a-tkinter-application


class Navbar(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent


class Toolbar(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent


class Statusbar(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.status_label = None
        self.parent = parent

    def set_status(self, label_text):
        self.status_label = None
        self.status_label = tk.Label(text=label_text)
        self.status_label.pack()


class Main(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent


class ITTMS(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.parent = parent

        self.toolbar = Toolbar(self)
        self.navbar = Navbar(self)
        self.main = Main(self)
        self.statusbar = Statusbar(self)

        self.statusbar.set_status("I am the status label")

        self.toolbar.pack(side="top", fill="x")
        self.navbar.pack(side="left", fill="y")
        self.main.pack(side="right", fill="both", expand=True)
        self.statusbar.pack(side="bottom", fill="x")


if __name__ == "__main__":
    root = tk.Tk()
    # root.geometry('800x600')
    ITTMS(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
