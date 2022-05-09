# Manpreet Singh | Student id - 632027 | Programming Task 8
import tkinter as tk

print('#############-----------Manpreet Singh | Student id - 632027 | Programming Task 9-----------###########')

# Distinction level callback function for Submit button
def print_greeting():
    print('Hi there,' + text_full_name.get())


# HD level callback function to check and compare emails
def email_check():
    if text_email.get() == '':
        print('Please enter your email address into the first field')
    elif text_email_again.get() == '':
        print('Please enter your email address into the second field')
    elif text_email.get() == text_email_again.get():
        print('You will receive an email shortly to confirm your membership')
    else:
        print('The email addresses entered do not match.')


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
                         height=10,
                         command=email_check
                         )

button_submit = tk.Button(text='Submit',
                          fg='black',
                          bg='white',
                          width=15,
                          height=10,
                          command=print_greeting
                          )

label_email = tk.Label(text='Enter email')
text_email = tk.Entry(bg='yellow',
                      fg='blue',
                      width=40
                      )

label_email_again = tk.Label(text='Enter email address again')
text_email_again = tk.Entry(bg='yellow',
                            fg='blue',
                            width=40
                            )

# Add the widgets to the window
label_welcome.pack()
label_full_name.pack()
text_full_name.pack()
label_email.pack()
text_email.pack()
label_email_again.pack()
text_email_again.pack()
button_submit.pack()
button_check.pack()

# Wait for the input from the user
pt9_window.mainloop()
