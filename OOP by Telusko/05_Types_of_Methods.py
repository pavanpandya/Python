# Three Types of Methods:
# 1. Instance Methods.
#     a. Accessor Methods - Will use when we want to Fetch the Value.
#     b. Mutator Methods - Will use when we want to Modify the Value.
# 2. Class Methods.
# 3. Static Methods.

class Student:

    school = "Ldrp-Itr"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        # Instance Method
        return (self.m1 + self.m2 + self.m3)/3

    def get_m1(self):
        # Accessor Method
        return self.m1

    def set_m1(self, value):
        # Mutator Method
        self.m1 = value

    @classmethod  # Decorator
    def getSchool(cls):
        # As you are working with class variable you have to use 'cls' as the parameter.
        return cls.school

    @staticmethod  # Decorator
    def info():
        # Something which is not concerned with the variables (Nothing to do with instance varaibles, Nothing to do with class varaibles)
        print("This is Student Class....")


s1 = Student(80, 85, 95)
s2 = Student(70, 95, 90)

print(s1.avg())
print(s2.avg())

print(Student.getSchool())
Student.info()
