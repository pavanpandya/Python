class PlayerCharacter:
    # They are Static
    membership = True  # Class Object Attribute

    def __init__(self, name="anaonymous", age=0):
        # This init Function gets call everytime when we instanciate the object.
        # Constructor Method
        # They are Dynamic
        self.name = name  # Instance attributes
        self.age = age

    def shout(self):
        print(f"My name is {self.name}")

    @classmethod  # Here cls is must to write
    def adding_things(cls, num1, num2):
        return num1 + num2
        # return cls('Tom', num1 + num2) #Here we have instanciated an object named tom with the value of (num1 + num2)

    @staticmethod  # We will use this when we don't want the cls or self.
    def greet():
        print("Hello, Good Morning")


PlayerCharacter.greet()
player1 = PlayerCharacter('Pavan', 19)
print(player1.name, player1.age)
# help(player1)   #This function will provide the entire blueprint of the object.
player1.shout()
# print(player1.adding_things(2,3)) --> This will throw an error "adding_things() takes 2 positional arguments but 3 were given.
# as in the definition we have not written cls as a parameter"
print(player1.adding_things(2, 3))
print(PlayerCharacter.adding_things(2, 3))

player2 = PlayerCharacter.adding_things(2, 3)
print(player2)
