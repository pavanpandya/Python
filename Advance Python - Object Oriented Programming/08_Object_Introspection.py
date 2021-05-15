class user(object):

    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print("Logged In")


class Wizard(user):

    def __init__(self, name, power, email):
        user.__init__(self, email)  # or super().__init__(email)
        # Here super refers to the super class and so we dont have to write self as a parameter
        self.name = name
        self.power = power

    def attack(self):
        print(f"Wizard is attacking with {self.power} power.")


class Archer(user):

    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"Archer is attacking with {self.power} arrows.")


wizard1 = Wizard('Merlin', 60, 'merlin@gmail.com')

print(dir(wizard1))
# This will give me all the methods and attributes wizard1 instance have.
