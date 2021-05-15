# Method Overloading:
# It Simply means if you have a class and in that class if you have lets say two methods with same name but diff parameters or arguments.
# eg:
# class Student:

#     def average(a, b):
#         pass

#     def average(a, b, c):
#         pass

'''But in python we dont have method overloading i.e We cannot create two methods with same name'''


class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self, a=None, b=None, c=None):
        s = 0
        if(a != None and b != None and c != None):
            s = a+b+c
        elif(a != None and b != None):
            s = a + b
        else:
            s = a

        return s


s1 = Student(58, 69)

print(s1.sum(5, 6, 7))

# In Function defining, we are taking 3 parameters with self but in print we have only pass two parameters with self.
# So to avoid the error we have defined all 3 variables as none.
print(s1.sum(5, 6))
print(s1.sum(5))
