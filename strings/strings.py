
print('Hello from Python!')
print()
print("Counts the number of letter 'm' in the the string")
dog_name = 'The dog is named Sammy'
dog_name_count = dog_name.count('m') #Counts the number of letter m in the the string
print(dog_name_count)
print()
print("String Concatenation and formatting")
first_name = 'Maduabughichi'
last_name = 'Achilefu'
print()
print('Formating strings using empty braces')
output = 'Hello, {} {}'.format(first_name, last_name) # Works in Python versions below 3.x
print(output)
print()
print('Formating strings using numbers with braces') # Works in Python versions below 3.x
output = 'Hello, {0} {1}'.format(first_name, last_name)
print(output)
print()
print('With numbers, you can interchange the strings order ')
output = 'Hello, {1} {0}'.format(first_name, last_name) 
print(output)
print()
print("Formating strings using 'f' keyword")
output = f'Hello {first_name} {last_name}' # Works in Python 3.x
print(output)
print()
print("Asking for user's input")
name = input('Please what is your name? ')
my_name = name.capitalize() # Capitalizing the first letter in string
print('Capitalizing the first letter in string')
print('Your name as provided is: '+my_name)
print()
print("Converting 'my_name' to lowercase") 
print(f'Your name as provided is: {my_name.lower()}')
print()
print("Converting 'my_name' to uppercase") 
print(f'Your name as provided is: {my_name.upper()}')
print()
print('Using single quotes inside double quotes to avoid errors')
print("It's a small world after all") 
print()
print('This is the end of the program. Thanks.')