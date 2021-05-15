# SUB CLASS CAN ACCESS ALL THE FEATURES OF SUPER CLASS
# BUT
# SUPER CLASS CANNOT ACCESS ANY FEATURES OF SUB CLASS

'''
IMPORTANT RULE:

When you create object of sub class it will call init of sub class first. 
If you have call super then it will first call init of super class and then call the init of sub class.

'''

# Rules : If you create object of sub class it will first try to find init of sub class,
# if it is not found then it will call init of super class.


class A:

    def __init__(self):
        print('INIt in A')

    def feature1(self):
        print("Feature-1 is Working")

    def feature2(self):
        print("Feature-2 is Working")


class B(A):

    def __init__(self):

        # If you also want to call the init method of class A then use 'super' keyword or you can say method.
        # By writing super we are representing super class A.
        super().__init__()
        print('INIt in B')

    def feature3(self):
        print("Feature-3 is Working")

    def feature4(self):
        print("Feature-4 is Working")


a1 = A()

# Here though it is the object of Class B, it is will call init method(Constructor of Class A)
# Because Class B was not having it's own init method. But after adding the init method, it will call it's own init method.
a2 = B()
