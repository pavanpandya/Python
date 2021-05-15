# Range - It returns an object that produces a sequence of integers from start(inclusive) to stop(exclusive) by step.
# Syntax:
# range(stop)
# range(start, stop[, step])

print(range(100))
# will give output:
# range(0, 100)

print(range(0, 100))
# will give output:
# range(0, 100)

for number in range(0, 100):
    print(number)
    # Will print the no. starting from 0 till 99

for _ in range(0, 10):
    print(_)
    # If you want don't need the variable then you can use underscore(_).
    # It indicates that hey i dont really care what's the variable name, I am just using range to get my desired output.

for _ in range(0, 10, 2):
    print(_)
    # Will print the no. starting from 0 till 9 and will step over the number by 2 (Be Default it is 1)

for _ in range(0, 10, -1):
    print(_)
    # Will not print anything

for _ in range(10, 0, -1):
    print(_)
    # Will print it in reverse order i.e 10 to 1

for _ in range(2):
    print(list(range(10)))
