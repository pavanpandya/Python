# Dictionary - It is data type and also the data structure in python
# It is unorderd key value pair (They are not all together in the memory like list)

Dictionary = {
    'a': 1,
    'b': 2
}
# Here a is key and 1 is Value

print(Dictionary['a'])
# This will print the value of key 'a'
print(Dictionary)
# This will print all the value of all the key

my_list = [
    {
        'a': 1,
        'b': 2
    },
    {
        'c': 3,
        'd': 4
    }
]

print(my_list[1]['c'])

my_list2 = [
    {
        'p': 1,
        'q': 'hello'
    },
    {
        'r': [1, 2, 3],
        's': True
    }
]

print(my_list2[1]['s'])
print(my_list2[1]['r'][1])

# ANOTHER WAY OF CREATING A DICTIONARY
# name = dict(key,value)
# user2 = dict('name'='Pavan') --> This will show an error
user2 = dict(name='Pavan')
print(user2)
