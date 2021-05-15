# They allow us to generate a sequence of values over time.

# eg: range()

range(10)
list(range(10))


def make_list(num):
    result = []
    for i in range(num):
        result.append(i)
    return result


my_list = make_list(10)
print(my_list)

# a list creates a giant list in the memory in one go
# whereas the range creates them one by one.

# iterable: is any object which can be loop through.
# iterate: The act of Iteration.
# generators: They are actually iterable.

# Note: Every Generator is iterable but not every iterable is a generator.
# Eg: Range is a generator which is iterable but a list is an iterable but not a generator.


def generator_function(num):
    for i in range(num):
        yield(i)

# What does Yield Do?
# - Yield pauses the function and comes back to it when we do something which is called "next".


for item in generator_function(10):
    print(item)

# Here instead of creating that List in the memory it just kept going one by one.
# We only held one item in the memory.

# Exploring Yield Keyword:


def generator_function2(num):
    for i in range(num):
        yield(i)


g = generator_function2(10)
next(g)  # 0
next(g)  # 1
next(g)  # 2
print(next(g))  # 3

# Note: Next can be called as many times as you want until we reach at the end of the range
# When we exceed the number it will show us stopiteration error.
