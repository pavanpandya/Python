# Tuple - They are like list but we cannnot change/ modify them. They are immutable.
# In tuple you can access the element just like list.

my_tuple = (1, 2, 3, 4, 5)

print(my_tuple)
print(5 in my_tuple)
print(my_tuple[2])

# tuple can be use as key in dictionary.
user = {
    (1, 2, 3): [1, 2, 3],
    'name': 'Pavan'
}
print(user[(1, 2, 3)])


new_tuple = my_tuple[:]
print(new_tuple)

x, y, z, *other = (1, 2, 3, 4, 5, 6)
print(x)
print(y)
print(z)
print(other)

# Methods
print(my_tuple.count(5))
print(my_tuple.index(5))
print(len(my_tuple))
