# == compares two values by evaluating them
# eg: in the example below 1 is converted into bool(1) which returns true and then both the values are compared. One of the two element gets
# Converted into second element type and then are evaluated.

print(True == 1)
# my_answer = True
# Correct_answer = True

print('' == 1)
# my_answer = False
# Correct_answer = False

print([] == 1)
# my_answer = False
# Correct_answer = False

print(10 == 10.0)
# my_answer = False
# Correct_answer = True

print([] == [])
# my_answer = True
# Correct_answer = True

print('1' == 1)
# Correct_answer = False

# == - checks for the equality of the value.
# is - checks that the value where they are stored in the memory are same or not?

print('1' is '1')
# They are two completely diff. lists stored at diff. places in the memory.
print([] is [])
print(True is True)

a = [1, 2, 3]
b = [1, 2, 3]
# They are two completely diff. lists stored at diff. places in the memory.
print(a is b)
