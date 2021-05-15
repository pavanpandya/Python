# Clean Code
# Good Readability
# NO Extra Stuff
# NO Random Camments
# Predictability
# DRY-DO Not Repeat Yourself

# Example- refer program no. 43
picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]

fill = '*'
empty = ' '
for row in picture:
    for pixel in row:
        if pixel:
            # Here we can directly write pixel bcus it can be either 1 or 0
            print(fill, end='')
        else:
            print(empty, end='')
    print(' ')
