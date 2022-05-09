# Manpreet Singh | Student id - 632027 | Programming Task 4

# Pass level
print('######-------Pass level--------#######')

# A comment with your name and student number
name_student_no = 'Manpreet Singh | 632027'

# A variable with the value of your full name in title case.
name_title_case = 'Manpreet Singh'

# A printout of the above string variable all in lowercase (note that you should use a string method).
print(name_title_case.lower())

# A printout of the output after using a method to make the string uppercase.
print(name_title_case.upper())

# A printout of the output after using a method to search your name string for the letter ‘a’.
is_a_in_name = 'a' in name_title_case
print('Is \'a\' in \'' + name_title_case + '\' : ' + str(is_a_in_name))

# A printout of the output after using a method to find the first two letters in your name.
first_two_letters = name_title_case[0:2]

print('First two letters are : \'' + first_two_letters + '\'')
print('---------------------------------------------------------------------\n')

# Credit level
print('######-------Credit level--------#######')

# Create and print (with key and value) a dictionary called Car with the following information:
# Make = Mitsubishi
# Model = Lancer
# Year = 2002
# Colour = Green
Car = {
    'Make': 'Mitsubishi',
    'Model': 'Lancer',
    'Year': 2002,
    'Colour': 'Green'
}
print(Car)

# Change the year to 2011 and the colour to blue
Car['Year'] = 2011
Car['Colour'] = 'blue'

# Print the car again.
print(Car)
print('---------------------------------------------------------------------\n')

# Distinction level
print('######-------Distinction level--------#######')

# Make a copy of the Car dictionary described above.
New_Car = Car.copy()

# To this dictionary copy, add the information Doors = 4.
New_Car['Doors'] = 4

# Print the new Car and the old Car.
print(New_Car)
print('---------------------------------------------------------------------\n')

# HD level
print('######-------HD level--------#######')

# Create a string and use a method to generate a description of the new car as shown below.
# Print it – it should be formatted like the text below (including the line breaks).
#
# Yesterday I bought a [Make] [Model].
# It’s not “too” old. It was made in [year] …
# I like it, though. It’s [colour], and it has [doors] doors!

templated_string = "Yesterday I bought a {} {}.\nIt's not \"too\" old. It was made in {} …\nI like it, though. It's {}, and it has {} doors!"
formatted_string = templated_string.format(New_Car['Make'], New_Car['Model'], New_Car['Year'], New_Car['Colour'], New_Car['Doors'])
print(formatted_string)