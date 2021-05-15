class Computer:

    def config(self):
        print("i5, 8gb, 1tb")


comp1 = Computer()  # This means that comp1 is the object of class Computer.
print(type(comp1))  # Gives the Output: <class '__main__.Computer'>

comp2 = Computer()

# Computer.config() --> This will throw an error as we have not defined for which object we are calling this Method/Function.
# Here you are passing comp1 as a argument and this comp1 is going in self.
Computer.config(comp1)
Computer.config(comp2)

# another way - Better way
comp1.config()
comp2.config()
# Here as you see we are not passing any argument but still it works because,
# behind the scene when you call comp1.config(), it takes comp1 as a argument and that goes/passes into self
