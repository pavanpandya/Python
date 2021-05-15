# Poly means 'Many' and Morph means 'Forms'.
# So That means one thing can take multiple forms.

# Four ways to Implement Polymorphism:
# 1 Duck Typing
# 2 Operator Overloading
# 3 Method Overloading
# 4 Method Overriding


'''Duck Typing - Looking at the below example, If there is an object which is ide and it has a method execute that's it
                 we are not concerned about which class object it is what we are concerned about is it should have that method in it.'''


class Pycharm:

    def execute(self):
        print("Compiling")
        print("Running")


class MyEditing:

    def execute(self):
        print("Spell Check")
        print("Convention Check")
        print("Compiling")
        print("Running")


class Laptop:

    def code(self, ide):
        ide.execute()


# ide = Pycharm()
ide = MyEditing()

# Here the type of ide is not fixed to Pycharm.
# We can change its type from Pycharm to MyEditing provided you have that method which is excuted.

# It doesn't matter which class object you are passing, what matters is that object should have execute method.
# This is called as Duck Typing.

lap1 = Laptop()
lap1.code(ide)
