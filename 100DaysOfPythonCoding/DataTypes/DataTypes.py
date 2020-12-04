# Data Types
# 1. String
# prints to the console the character at index 4
print("Hello"[4])
print("123" + "456")

# 2. Integer
print(123 + 456)
# Python ignores the under that serves as commas and prints the number
print(123_456_789)

# 3. Float
print(3.12534)

# 4. Boolean
print(True)
print(False)

# Type Checking
name = "Madu"
num1 = 123
print(type(name))
print(type(num1))

# Type Conversion or Casting
print(str(123) + str(456))
print(float(70))
print(int(7.2))

# Challenge 1
two_digit_number = input("Type a two-digit number!\n")
sum_of_two_digit_num = int(two_digit_number[0]) + int(two_digit_number[1])
print(sum_of_two_digit_num)

