# Rules While Giving Parameters in Function Definition (Order): Parameters, *args, Default Parameters, **kwargs.
# eg: def test(name, *args, i='Hello', **kwargs)

'''*argument(*args) - By placing * in front of parameter while definiting the function will allow the function to take as many parameter as the user want.'''


def super_func(*args):
    # will print in form of tuple
    print(args)
    return sum(args)


print(super_func(1, 2, 3, 4, 5))

''' **keyword_argument(**kwargs) - By placing ** in front of parameter while definiting the function will allow the function to take as many keyword arguments as paramater as the user want.
'''


def sup_func(**kwargs):
    # will print in form of Dictionary
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


sup_func(num1=1, num2=2, num3=3)


# Combination of Both
def myfun(*args, **kwargs):
    # will print in form of tuple
    print("Args: ", args)
    # will print in form of Dictionary
    print("Kwargs: ", kwargs)


myfun('Geeks', 'For', 'Geeks', name='Pavan', branch='CS')


# Combination of Both
def su_func(*args, **kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total


print(su_func(1, 2, 3, 4, 5, num1=1, num2=2, num3=3))
