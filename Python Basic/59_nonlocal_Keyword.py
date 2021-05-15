# nonlocal - not a global variable but outside the scope of my function.

def outer():
    x = 'local'

    def inner():
        nonlocal x
        # Grabbing the value of x from parent local scope
        x = 'nonlocal'
        # Reassigning the value of x from local to nonlocal
        print('Inner:', x)

    inner()
    print('Outer:', x)


def outer1():
    x1 = 'local'

    def inner1():
        # This x1 is diff than the one in outer1 function.
        x1 = 'nonlocal'
        print('Inner1:', x1)

    inner1()
    print('Outer1:', x1)


print('Using nonlocal keyword')
outer()
print(' ')
print('Without Using nonlocal keyword')
outer1()
