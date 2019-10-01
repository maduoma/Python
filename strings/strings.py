
print('Hello from Python!')
print()
print('Counts the number of letter m in the the string')
dog_name = 'The dog is named Sammy'
dog_name_count = dog_name.count('m') #Counts the number of letter m in the the string
print(dog_name_count)
print()
print("String Concatenation and formatting")
print()
first_name = 'Maduabughichi'
last_name = 'Achilefu'
print('Formating strings using empty braces')
print()
output = 'Hello, {} {}'.format(first_name, last_name) # Works in Python versions below 3.x
print(output)
print()
print('Formating strings using numbers') # Works in Python versions below 3.x
output = 'Hello, {0} {1}'.format(first_name, last_name)
print(output)
print()
output = 'Hello, {1} {0}'.format(first_name, last_name) # With numbers, you can interchange the strings order 
print(output)
print()
print('Formating strings using f keyword')
output = f'Hello {first_name} {last_name}' # Works in Python 3.x
print(output)
print()
print("Asking for use's input")
name = input('Please what is your name? ')
# Capitalizing the first letter in string 
my_name = name.capitalize()
print('Your name as provided is: '+my_name)
print()
print('Converting my_name to lowercase') 
print(f'Your name as provided is: {my_name.lower()}')
print()
print('Converting my_name to uppercase') 
print(f'Your name as provided is: {my_name.upper()}')
print()
print("It's a small world after all")
print('This is the end of the program. Thanks.')