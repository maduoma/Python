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
country = input('Which country do you live in? ')
if country.lower() == 'canada':
    province = input('Which province do you live in? ')
    if province.lower() in('Alberta',\
        'Nunavut', 'Yukon'):
        tax = 0.05
    elif province.lower() == 'Ontario':
        tax = 0.15
    else:
        tax = 0.15
else:
   tax = 0
print(f'Your tax is {tax}')

