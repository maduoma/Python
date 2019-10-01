
print('Hello from Python!')
print()
dog_name = 'The dog is named Sammy'
dog_name_count = dog_name.count('m') #Counts the number of letter m in the the string
print(dog_name_count)
first_name = 'Maduabughichi'
last_name = 'Achilefu'
# output = 'Hello, {} {}'.format(first_name, last_name)
# output = 'Hello, {0} {1}'.format(first_name, last_name)
output = f'Hello {first_name} {last_name}'
print(output)
name = input('Please what is your name? ')
# Capitalizing the first letter in string 
my_name = name.capitalize()
print('Your name as provided is: '+my_name)
print(f'Your name as provided is: {my_name.lower()}')
print(f'Your name as provided is: {my_name.upper()}')
print("It's a small world after all")
print('This is the end of the program. Thanks.')