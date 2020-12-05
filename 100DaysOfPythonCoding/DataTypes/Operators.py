#################################################################
# Mathematical Operations
#################################################################
# Addition
print(1 + 2)

# Subtraction
print(2 - 1)

# Multiplication
print(2 * 3)

# Division
# # Gives a float in Python
print(4 / 2)

# Exponent or raising a number to a power
# Getting a hold of 3 to the power of 2
print(3 ** 2)

#################################################################
# Operator Precedence
#################################################################
# PEMDAS(LR) - Parentheses Exponents Multiplication Division Addition Subtraction (Left to Right)
# BODMAS(LR) - Bracket Of Division Multiplication Addition Subtraction (Left to Right)

# When it comes to calculation, 'Multiplication & Division' and 'Addition & Subtraction' are both equally
# important, the calculation that is most to the left is the one that will be prioritized between Multiplication and
# Division and between Addition and Subtraction, the calculation goes from left to right as shown below:
print(3 * 3 + 3 / 3 - 3)
print(3 / 3 - 3 * 3 + 3)
print(3 * (3 + 3) / 3 - 3)

#################################################################
# Challenge 2.2: BMI
#################################################################
height = input("Enter your height in m: \n")
weight = input("Enter your weight in kg: \n")
my_height = float(height)
my_weight = int(weight)
BMI = my_weight / (my_height ** 2)
my_bmi = int(BMI)
print("Your BMI is " + str(my_bmi) + "\n")


#################################################################
# Mathematical operations:  More on Operators : Data Manipulations
#################################################################
#
print((8 / 3))
print(type(round(8 / 3)))
# Adds two decimal places to the result
print(round(8 / 3, 2))
print(type(round(8 / 3, 2)))
# Floor Division gives a whole number integer and discards all the numbers after decimal places
print(8 // 3)
print(type(8 // 3))
# Rounds the number to 2 decimal places
print(round(2.66666666666, 3))
# f-String : Helps to eliminate all the hassles or pains of type conversion to string, etc, before printing to the
# console. It uses curly braces {} to mix variables and prints to the console without breaking the code e.g
score = 2
height = 9
isWinning = True
print(f"Your score is {score}, your height is {height}, your winning is {isWinning}\n")

#################################################################
# Challenge 2.3 # You have x days, y weeks, and z months left if you've 90 years to live
#################################################################
current_age = input("What is your current age? \n")
remaining_years = 90 - int(current_age)
remaining_years_in_days = remaining_years * 365
remaining_years_in_weeks = remaining_years * 52
remaining_years_in_months = remaining_years * 12
print(f"You have {remaining_years_in_days} days, {remaining_years_in_weeks} weeks and {remaining_years_in_months} "
      f"months left.\n")

#################################################################
# Challenge 2.4 : Tip Calculator
#################################################################
# Welcome to the Tip Calculator.
# What was the total bil? $124.56
# What percentage tip would you like to give? 10, 12, or 15? 12
# How many people to split the bill? 7
# Each person should pay: $19.93
print("Welcome to Tip Calculator.")
total_bill = input("What was the total bill? $")
total_bill = float(total_bill)
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
tip = float(tip) / 100
total_bill_in_percentage = total_bill * tip
payable_bill = total_bill + total_bill_in_percentage
number_of_people_to_split_bill = input("How many people to split the bill? ")
number_of_people_to_split_bill = int(number_of_people_to_split_bill)
what_each_person_pays = payable_bill / number_of_people_to_split_bill
what_each_person_pays_in_2_decimal_places = round(what_each_person_pays, 2)
print(f"Each person should pay ${what_each_person_pays_in_2_decimal_places}")


