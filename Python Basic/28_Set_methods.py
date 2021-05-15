my_set = {1, 2, 3, 4, 5}
your_set = {4, 5, 6, 7, 8, 9}

print(my_set.difference(your_set))
# # difference between my_set and your_set when viewed from my_set
print(my_set)
# # Here my_set is not modified

print(my_set.difference_update(your_set))
print(my_set)
# # Here my_set is modified

print(my_set.intersection(your_set))
print(my_set & your_set)
# Short hand for Intersection
print(my_set)

print(my_set.isdisjoint(your_set))
# # here it show that do they have anything in common and if yes it prints false and if it prints true i.e they have nothing in common

print(my_set.union(your_set))
print(my_set | your_set)
# Short hand for Union
print(my_set)

print(my_set.issubset(your_set))
# return true or False

print(your_set.issuperset(my_set))
# return true or False

print(my_set.discard(5))
print(my_set)

# Use the correct method to add multiple items (more_fruits) to the fruits set.
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
