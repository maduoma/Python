price = input('How much did you pay?  ')
price = float(price)
if price >= 1.00:
    tax = .07
    print(f'The task rate is {tax}')
else:
    tax = 0
    print(f'The task rate is {tax}')
# OR
if price >= 1.00:
    tax = .07
else:
    tax = 0
print(tax)

# For Strings
country = input('Which country are you from? ')
if country.lower() == 'canada':
    print('Oh, you are a Canadian!')
else:
    print('You are not from Canada. This offer is not for you!')

