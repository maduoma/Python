from datetime import datetime, timedelta

print('Hello from Python!')
print()
name = input('Please what is your name? ')
# Capitalizing the first letter in string 
my_name = name.capitalize()
print('Your name as provided is: '+my_name)
print('This is the end of the program. Thanks.')

print('Adding numbers') 
x = 34 + 4
print(x)
print('Dividing numbers') #USE this comment to debug or detect where errors occur in your code easily
y = x / 2
print(y)
dog_name = 'The dog is named Sammy'
dog_name_count = dog_name.count('m') #Counts the number of letter m in the the string
print(dog_name_count)
first_name = 'Maduabughichi'
last_name = 'Achilefu'
# output = 'Hello, {} {}'.format(first_name, last_name)
# output = 'Hello, {0} {1}'.format(first_name, last_name)
output = f'Hello, {first_name} {last_name}'
print(output)
print("It's a small world after all")
print('This is the end of the program')

today = datetime.now()
# print(f'Today is {today}')
print('Today is: '+str(today))

one_day_ago = timedelta(days = 1)
yesterday = today - one_day_ago
print(f'Yesterday was {yesterday}')
two_days_ago = timedelta(days = 2)
the_day_before_yesterday = today - two_days_ago
print(f'The day before yesterday was {the_day_before_yesterday}')

current_date = datetime.now()
print(f'Day: {current_date.day}')
print(f'Month: {current_date.month}')
print(f'Year: {current_date.year}')

birthday = input('When is your birthday (dd/mm/yyyy)? ')
my_birthday = datetime.strptime(birthday, '%d/%m/%Y')
print(f'Birthday: {my_birthday}')

one_week_ago = timedelta(weeks = 1)
one_week_ago_date = current_date - one_week_ago
print(f'Last Week (One Week Ago): {one_week_ago_date}')
