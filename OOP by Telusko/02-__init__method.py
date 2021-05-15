class Computer:

    def __init__(self, cpu, ram):
        # It will be called automatically.
        # For every object, it is called once.
        self.cpu = cpu
        self.ram = ram

    def config(self):
        # print("Config is ", cpu, ram) -->This will throw an error as they are not local variables.
        # They belong to an Object and are refered using self.
        print("Config is ", self.cpu, self.ram)


# Here we have 2 objects and each objects will have their own variables.
comp1 = Computer("i5", 16)
comp2 = Computer("ryzen3", 8)
# Now here question arises that we are passing 2 arguments and the method takes 3 parameters?
# So, Here comp1 is passed automatically(by default) so behind the scenes it looks like this-->comp1 = Computer(comp1,"i5", 16)

comp1.config()
comp2.config()
