# Manpreet Singh | Student id - 632027 | Programming Task 3.
print('#############-----------Manpreet Singh | Student id - 632027 | Programming Task 3.-----------###########')
# Pass level
# Declaration of variables.
first_variable = int(3)
second_variable = int(7)

# The first and second variables added together.
result_addition = first_variable + second_variable
print('######-------Pass level--------#######')
print('The first (' + str(first_variable) + ') and second (' + str(
    second_variable) + ') variables added together : ' + str(result_addition))

# The first variable subtracted from the second variable.
result_subtraction = second_variable - first_variable
print(
    'The first variable(' + str(first_variable) + ') subtracted from the second variable(' + str(first_variable) + ') '
                                                                                        ': ' + str(result_subtraction))

# A check to see if the values of the two variables are equal.
result_comparison = first_variable == second_variable
print('A check to see if the values of the two variables are equal : ' + str(result_comparison))
print('---------------------------------------------------------------------\n')

# Credit level
print('######-------Credit level--------#######')

# A check to see if the second variable is less than 10, and the result printed to screen without creating a new
# variable.
result_second_variable_less_then_ten = second_variable < 10
print('Is second variable(' + str(second_variable) + ') less than 10 : ' + str(result_second_variable_less_then_ten))

# Both variables added together then 5 subtracted from the sum, and the result printed to screen without
# creating a new variable.
result_both_added_5_subtracted = (first_variable + second_variable) - 5
print('Both variables added then 5 subtracted : ' + str(result_both_added_5_subtracted))
print('---------------------------------------------------------------------\n')

# Distinction level
print('######-------Distinction level--------#######')

# Both variables compared to the number 10 to check that BOTH variables are less than or equal to 10.
is_first_variable_lt_ten = first_variable <= 10
is_second_variable_lt_ten = second_variable <= 10
print('Is first variable(' + str(first_variable) + ') LT or equal to ten : ' + str(is_first_variable_lt_ten))
print('Is second variable(' + str(second_variable) + ') LT or equal to ten : ' + str(is_second_variable_lt_ten))

# The opposite of the operation above.
is_first_variable_gt_ten = first_variable >= 10
is_second_variable_gt_ten = second_variable >= 10
print('Is first variable (' + str(first_variable) + ')GT or equal ten : ' + str(is_first_variable_gt_ten))
print('Is second variable(' + str(second_variable) + ') GT or equal to ten : ' + str(is_second_variable_gt_ten))
print('---------------------------------------------------------------------\n')

# HD Level
print('######-------HD level--------#######')

# A third variable with the value 2.4 and a fourth variable with the value 5.4 which are both cast to float.
third_variable = float(3.4)
fourth_variable = float(5.4)

# An operation that works out if the product of the third and fourth variables is greater than the product
# of the first and second variables. (The term ‘product’ is a mathematical term that refers to the result of
# one or more multiplications – in this case two variables multiplied together.)
product_first_second_variable = first_variable * second_variable
product_third_fourth_variable = third_variable * fourth_variable
is_product_third_fourth_greater = product_third_fourth_variable > product_first_second_variable
print('Is product of third and fourth variable(' + str(product_third_fourth_variable) + ') is greater than first and '
                    'second(' + str(product_first_second_variable) + ') : ' + str(is_product_third_fourth_greater))
