from functools import reduce

my_list = [1, 2, 3]


def accumulator(acc, item):
    print(acc, item)
    return item + acc


print(reduce(accumulator, my_list, 0))
# Here 0 is initial.
