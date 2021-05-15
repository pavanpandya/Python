# Inheritance = Parent-Child Relationship

'''MULTI-LEVEL INHERITANCE'''

# IN THE EXAMPLE BELOW:
# CLASS A IS SUPER CLASS OR GRAND-PARENT CLASS,
# CLASS B IS SUB CLASS OR CHILD CLASS OF A AND PARENT CLASS OF C,
# CLASS C IS SUB CLASS OR CHILD CLASS OF B.


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


# This means that class C is inheriting all the features of class B and A  or we can say C is a Child/Sub Class of B.
class C(B):

    def feature5(self):
        print("Feature-5 is Working")


a1 = A()

a1.feature1()
a1.feature2()

b1 = B()

# Here b1 is able to access all the Functionality of Class A as Class B is child of Class A.
b1.feature1()
b1.feature2()
b1.feature3()
b1.feature4()

c1 = C()

# Here c1 is able to access all the Functionality of Class A and Class B as Class C is child of Class B and Class B is child of Class A.
c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
c1.feature5()
