# Set-Unordered Collection of unique objects

my_set = {1, 2, 3, 4, 5, 6}
print(my_set)

# Now let say we have an another set name my_set2
my_set2 = {1, 2, 3, 4, 5, 5}
print(my_set2)
# Here this will only print the unique objects.

my_set.add(100)
my_set.add(2)
# Here 2 is not added in the set because it is already present in the set.
print(my_set)

# print(my_set[0]) #This will throw an error as we can't access the elements like this.
print(len(my_set))
print(2 in my_set)

# Trick
my_list = [1, 2, 3, 4, 5, 6, 5]
print(set(my_list))

new = my_set2.copy()
print(new)
print(list(new))
