class Computer:
    def __init__(self):
        self.name = 'Pavan'
        self.age = 19

    def update(self):
        self.age = 20

    def compare_Age(self, other):
        if self.age == other.age:
            return True


c1 = Computer()
# print(id(c1)) This gives the address of c1(which is stored in the heap memory)
c2 = Computer()
# print(id(c2)) This gives the address of c2(which is stored in the heap memory)

# Every time you create an object, it is allocated a new space.
# Thus, we get to know that both the objects are created in diff memory location.

# Size of variables depends on the no. of variables

# Who allocates the size to object?
# -->Constructor.
# so whenever you write c1 = Computer(), Computer() is your Constructor and this will call init method for you.

c2.name = 'Astha'
c2.age = 13

c1.update()
# As, you see we are not passing any arguments.
# Now the moment at which the interpreter comes to the line c1.update(), it will get pointed/Focused to the above method named update().
# So by using self as a parameter, which acts as an pointer or you can say self is directing to c1 or c2 based on what you are calling.
# So by writing c1.update(), the self will point to c1 and now the update() will run on the c1 object.

print(c1.name, c1.age)
print(c2.name, c2.age)

# Here compare_Age() looks like compare_Age(who is callinng, with whom to compare)
if c1.compare_Age(c2):
    print("They are Identical.")
else:
    print("They are not Identical.")
