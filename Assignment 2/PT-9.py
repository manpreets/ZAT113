# Manpreet Singh | Student id - 632027 | Programming Task 8
import tkinter as tk

# Distinction level callback function for Submit button
def print_greeting():
    print('Hi there,' + text_full_name.get())


# Pass level.
pt9_window = tk.Tk()
pt9_window.geometry('800x600')

pt9_window.title('ZAT113 Task 9')
label_welcome = tk.Label(text='Welcome to this page. Please enter your details below')
label_full_name = tk.Label(text='Full name : ')
# End pass level

# Start credit level
text_full_name = tk.Entry(bg='blue',
                          fg='yellow',
                          width=30)

# Credit and distinction levels
button_check = tk.Button(text='Check',
                         fg='black',
                         bg='white',
                         width=15,
                         height=10
                         )

button_submit = tk.Button(text='Submit',
                          fg='black',
                          bg='white',
                          width=15,
                          height=10,
                          command=print_greeting
                          )

text_email = tk.Entry(text='Email Address',
                      bg='yellow',
                      fg='blue',
                      width=40
                      )


# Add the widgets to the window
label_welcome.pack()
label_full_name.pack()
text_full_name.pack()
button_submit.pack()
button_check.pack()
text_email.pack()

# Wait for the input from the user
pt9_window.mainloop()


