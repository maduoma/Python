#########################################
# If statement
#########################################
print("Welcome to rollercoaster!")
height = int(input("what is your height? "))
if height >= 120:
    print("You can ride coaster")
else:
    print("You will have to grow taller to be able to ride.")
print("\n")

#########################################
# Challenge 3.1 : Even or Odd Number
#########################################
num = int(input("Enter a number? "))
if num % 2 == 0:
    print("Number entered is an even number!")
else:
    print("Number entered is an odd number")
print("\n")

#########################################
# Nested if/else statement
#########################################
print("Welcome to rollercoaster!")
height = int(input("what is your height? "))
if height >= 120:
    print("You can ride coaster")
    age = int(input("What is your age?"))
    if age >= 18:
        print("Please pay $7")
    else:
        print("Please pay $5")
else:
    print("You will have to grow taller to be able to ride.")
print("\n")

#########################################
# elif between if -- else as many as required
#########################################
print("Welcome to rollercoaster!")
height = int(input("what is your height? "))
if height >= 120:
    print("You can ride coaster")
    age = int(input("What is your age?"))
    if age < 12:
        print("Please pay $5")
    elif age <= 18:
        print("Please pay $7")
    else:
        print("Please pay $12")
else:
    print("You will have to grow taller to be able to ride.")
print("\n")

#########################################
# Challenge 3.2 : Day 3.2 - BMI Calculator 2.0
#########################################
print("Welcome to BMI Calculator!")
height = float(input("Please enter your height?\n"))
weight = float(input("Please enter your weight?\n"))
bmi = round(weight / (height ** 2))
# bmi = 35
if bmi < 18.5:
    print(f"Your bmi is {bmi}, you're underweight!")
elif bmi < 25:
    print(f"Your bmi is {bmi}, you have a normal weight!")
elif bmi < 30:
    print(f"Your bmi is {bmi}, you're overweight!")
elif bmi < 35:
    print(f"Your bmi is {bmi}, you're obese!")
else:
    print(f"Your bmi is {bmi}, you're clinically obese!")
print("\n")

#########################################
# Challenge 3.3 : Day 3.3 - Leap Year
#########################################
print("Welcome to Leap Year Challenge!")
year = int(input("Which year do you want to check? "))
if year % 4 == 0:
    print(f"{year} is leap year.")
elif year % 100 == 0:
    print(f"{year} is not leap year.")
elif year % 400 == 0:
    print(f"{year} is leap year.")
else:
    print(f"{year} is not leap year.")
print("\n")

# import calendar
# print(calendar.isleap(1900))
# OR
print("Welcome to Leap Year Challenge!")
year = int(input("Which year do you want to check? "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is leap year!")
        else:
            print(f"{year} is not leap year!")
    else:
        print(f"{year} is leap year!")
else:
    print(f"{year} is not leap year!")
print("\n")
