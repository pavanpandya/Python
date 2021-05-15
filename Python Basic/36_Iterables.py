# String, List, Dictionary, Tuple, Set can be Iterable.
# Iterate means we go one by one to check each item in the collection.

user = {
    'name': 'Pavan',
    'age': 19,
    'can_swim': False
}

for item in user.items():
    key, value = item  # Tuple Unpacking
    print(key, value)

# ShortHand for Tuple Unpacking is :
# for key, value in user.item():
#     print(key, value)

for item in user.values():
    print(item)

for item in user.keys():
    print(item)
