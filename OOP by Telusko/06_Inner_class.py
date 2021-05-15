# You can create object of inner class inside the outer class
# or
# You can create object of inner class outside the outer class provided you use the outer class name to call it.

class Student:

    def __init__(self, name, rollno):
        self.name = name
        self. rollno = rollno
        self.lap = self.laptop()  # Defining the object of inner-class Laptop.

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()

    class laptop:  # Inner Class

        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = '8gb'

        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = Student('Pavan', 1)
s2 = Student('Deep', 2)

# print(s1.name, s1.rollno)
s1.show()
# print(s2.name, s2.rollno)
s2.show()

# lap1 = Student.laptop() #When you create object outside the outer class.
lap1 = s1.lap
lap2 = s2.lap

print(s1.lap.brand)
print(s2.lap.ram)
