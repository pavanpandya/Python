class PlayerCharacter:
    # They are Static
    membership = True  # Class Object Attribute

    def __init__(self, name="anaonymous", age=0):
        # This init Function gets call everytime when we instanciate the object.
        # Constructor Method
        if age > 18:
            # if PlayerCharacter.membership: Both PlayerCharater.membership and self.membership are valid
            # They are Dynamic
            self.name = name  # Instance attributes
            self.age = age

    def shout(self):
        print(f"My name is {self.name}")


player1 = PlayerCharacter('Pavan', 19)
print(player1.name, player1.age)
# help(player1)   #This function will provide the entire blueprint of the object.
player1.shout()
