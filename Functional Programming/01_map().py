# map(action, data)
# This means that what sort of action you want to take on your data.

my_list = [1, 2, 3]


def multiply_by_2(item):
    return item*2


print(list(map(multiply_by_2, [1, 2, 3])))
print(list(map(multiply_by_2, my_list)))
# Map gives us the object at particular location.
# so we have to typecast it to list to get the output.
# Also, here we are not calling the multiply_by_2 function, map function does that for us.

print(my_list)
# Here the actual list will remain unchanged.
