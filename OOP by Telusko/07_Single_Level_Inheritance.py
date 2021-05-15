# Inheritance = Parent-Child Relationship

'''SINGLE LEVEL INHERITANCE'''

# IN THE EXAMPLE BELOW:
# CLASS A IS SUPER CLASS OR PARENT CLASS AND,
# CLASS B IS SUB CLASS OR CHILD CLASS.


class A:

    def feature1(self):
        print("Feature-1 is Working")

    def feature2(self):
        print("Feature-2 is Working")


# This means that class B is inheriting all the features of class A or we can say B is a Child/Sub Class of A.
class B(A):

    def feature3(self):
        print("Feature-3 is Working")

    def feature4(self):
        print("Feature-4 is Working")


a1 = A()

a1.feature1()
a1.feature2()

b1 = B()

# Here b1 is able to access the Functionality of Class A as Class B is child of Class A.
b1.feature1()
b1.feature2()
b1.feature3()
b1.feature4()
