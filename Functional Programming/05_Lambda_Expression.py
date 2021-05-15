# lambda param: action(param)

from functools import reduce

my_list = [1, 2, 3]
print(list(map(lambda item: item*2, my_list)))
print(list(filter(lambda item: item % 2 != 0, my_list)))
print(reduce(lambda acc, item: acc + item, my_list))

# List Sorting
a = [(0, 2), (4, 3), (9, 9), (10, -1)]

a.sort(key=lambda x: x[0])
# Will sort based on first key
print(a)
a.sort(key=lambda x: x[1])
# Will sort based on second key
print(a)
