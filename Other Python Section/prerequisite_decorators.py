# @classmethod
# @staticmethod

# are the example of decorators.

def hello():
    return 'hello Good Morning!'


greet = hello
greet1 = hello()

# Will Print the Address at which hello function is present.
print(greet)
# Will Print Output.
print(greet1)


def greeting(func):
    return func()


def msg():
    return 'Printing from msg function!'


a = greeting(msg)
print(a)
