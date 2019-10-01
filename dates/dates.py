# importing Date library
from datetime import datetime, timedelta
# Getting today's date
today = datetime.now()
# f keyword converts date to a string before printing
print(f'Today is {today}')
# Alternative  way to convert date to a string before printing
print('Today is: '+str(today))
# timedelta is used to get a period of time and used with datetime to get the present, past or future time, like yesterday, birthday, etc
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
print("Today's date is "+ str(current_date)) #Converting current date to string before printing
