# Decorator -
# Always begins with '@'.
# Super charges the function.
# It simply a function that wrap another function and enhances it.
# It simply just add more functionality to the function.

def my_decorator(func):
    def wrap_func():
        print('************')
        func()
        print('************')
    return wrap_func


@my_decorator
def hello():
    print('Hello')


@my_decorator
def bye():
    print('See ya later')


hello()
bye()


# Mechanism:
# @my_decorator
# def hello():
#     print('Hello')

# The above code is equal to below code written:


def hello2():
    print('Hello')


a = my_decorator(hello2)
a()
