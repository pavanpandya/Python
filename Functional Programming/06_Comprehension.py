# List Comprehension:

my_list = []

for char in 'Good Morning':
    my_list.append(char)

print(my_list)

# Faster way of doing this

# Syntax:
# my_list = [param for param in iterable]

my_list = [char for char in 'Good Morning']
print(my_list)

my_list2 = [num for num in range(0, 10)]
print(my_list2)

my_list3 = [num*2 for num in range(0, 10)]
print(my_list3)

my_list4 = [num for num in range(0, 10) if num % 2 == 0]
print(my_list4)


# Set Comprehension.
my_set = {char for char in 'Good Morning'}
print(my_set)

my_set2 = {num for num in range(0, 10)}
print(my_set2)

my_set3 = {num*2 for num in range(0, 10)}
print(my_set3)

my_set4 = {num for num in range(0, 10) if num % 2 == 0}
print(my_set4)


# Dictionary Comprehension.

simple_dict = {
    'a': 1,
    'b': 2
}

my_dict = {key: value**2 for key, value in simple_dict.items()}
print(my_dict)

my_dict2 = {key: value**2 for key, value in simple_dict.items() if value %
            2 == 0}
print(my_dict2)

my_dict3 = {num: num*2 for num in [1, 2, 3]}
print(my_dict3)


# Exercise.

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

# duplicates = []
# for value in some_list:
#     if some_list.count(value) > 1:
#         if value not in duplicates:
#             duplicates.append(value)
# print(duplicates)

# Giving Solution using List Comprehension:
duplicates = list(
    set({value for value in some_list if some_list.count(value) > 1}))
print(duplicates)
