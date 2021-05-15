# For Loop - It allows us to iterate over anything that has collection of items.

# Syntax: for target_list in expression_list:
#            pass

# Examples:

# String
for item in 'Zero To Mastery':
    print(item)

# List
for item in [1, 2, 3, 4, 5]:
    print(item)

# Set
for item in {1, 2, 3, 4, 5}:
    print(item)

# Tuple
for item in (1, 2, 3, 4, 5):
    print(item)

# Nested Loops:
for items in (1, 2, 3, 4, 5):
    for x in ['a', 'b', 'c']:
        print(items, x)
