# Inheritance = Parent-Child Relationship

'''MULTIPLE INHERITANCE'''

# IN THE EXAMPLE BELOW:
# CLASS A IS SUPER CLASS OR PARENT CLASS OF CLASS C AND,
# CLASS B IS SUPER CLASS OR PARENT CLASS OF CLASS C,
# CLASS C IS SUB CLASS OR CHILD CLASS OF A AND CLASS B.


class A:

    def feature1(self):
        print("Feature-1 is Working")

    def feature2(self):
        print("Feature-2 is Working")


class B:

    def feature3(self):
        print("Feature-3 is Working")

    def feature4(self):
        print("Feature-4 is Working")


# This means that class C is inheriting all the features of class A and class B
class C(A, B):

    def feature5(self):
        print("Feature-5 is Working")


a1 = A()

a1.feature1()
a1.feature2()

b1 = B()

b1.feature3()
b1.feature4()

c1 = C()

# Here c1 is able to access all the Functionality of Class A and Class B as Class C is child of Class A and Class B.
c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
c1.feature5()
