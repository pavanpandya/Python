# Introduction
def say_hello():
    print("Hello Good Morning")


say_hello()

picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]


def show_tree():
    for row in picture:
        for pixel in row:
            if(pixel == 1):
                print('*', end='')
            else:
                print(' ', end='')
        print(' ')


show_tree()
show_tree()
# The below print give the memory location of show_tree
# print(show_tree)
