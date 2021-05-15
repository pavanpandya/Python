# OOP - Object Oriented Programming

# Class - Blueprint.
# Object - Instance of Class.(Instanciation)

class BigObject:
    # Code
    pass


obj1 = BigObject()  # instanciate
obj2 = BigObject()  # instanciate
obj3 = BigObject()  # instanciate
print(type(obj1))


# Creating our Own Class:
class PlayerCharacter:
    def __init__(self, name, age):
        # Constructor Method
        self.name = name #attributes
        self.age = age

    def run(self):
        print("Run")


player1 = PlayerCharacter('Pavan', 19)
player2 = PlayerCharacter('Astha', 13)
print(player1.name)
print(player1.age)
print(player2.name)
print(player2.age)
