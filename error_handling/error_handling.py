x = 67
y = 0
try:
    print(x / y)
except ZeroDivisionError as e:
    print('Division by zero is not allowed!')
else:
    print('Oops, Something went wrong!')
finally:
    print('Try again!')