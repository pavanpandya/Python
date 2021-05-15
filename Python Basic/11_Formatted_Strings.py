# Formatted Strings

name = 'Pavan'
age = 19
# print('Hi' + name + '. You are ' + age + ' year old.') --> This will throw an error as age is int
# and string Concatenation only works with strings
print('Hi ' + name + '. You are ' + str(age) + ' year old.')

# Better Way of doing This
print(f'Hi {name}. You are {age} year old.')  # Formatted Strings

# print('Hi {}. You are {} year old.').format('Pavan', '19') --> This will throw an error as it
# will run for print and not for the elements in print.
print('Hi {}. You are {} year old.'.format('Pavan', '19'))
# This also works the same as above
print('Hi {}. You are {} year old.'.format(name, age))

# printing other variable
print('Hi {new_name}. You are {age} year old.'.format(
    new_name='John', age='20'))
