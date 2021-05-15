# Higher Order Function HOC

# -It can either be a function which accepts other function as parameter.

def greet(func):
    func()


# - This is the example of HOC.

# -If it's a function which returns another function.

def greet1():
    def func():
        return 5
    return func

# - This is an another example of HOC.

# map,reduce, filter all are examples of Higher Order Function.
