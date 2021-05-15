user = {
    'basket': [1, 2, 3],
    'greet': 'Hello',
    'year': 2020
}

print(user.get('age'))
# Here though age (key) is not present, "print(user.get('age'))" this will not throw an error
# because .get returns the value if key is there else it returns none.

# You can also add an default value in get method (in case if you don't want to print none)
print(user.get('age', 'The key is not present'))

# ANOTHER WAY OF CREATING A DICTIONARY
# name=dict(key,value)
# user2 = dict('name'='Pavan') --> This will show an error
user2 = dict(name='Pavan')
print(user2)
user2 = user.copy()
print(user2)

print('basket' in user)
print(user.keys())
print(user.values())
print(user.items())
print(user.update({'year': 2021}))
# Here if year exist then it will modify the value or else it will add the key 'year' to the dictionary
# print(user.pop('greet'))
print(user.popitem())  # It remove any random key-value pair
print(user.clear())

# Change the "year" value from 1964 to 2020.
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car["year"] = 2020

# Add the key/value pair "color" : "red" to the car dictionary.
car["color"] = "red"
