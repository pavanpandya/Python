'''
IMPORTANT RULE:

When you create object of sub class it will call init of sub class first. 
If you have call super then it will first call init of super class (from Left to Right) and then call the init of sub class.

'''

# Rules : If you create object of sub class it will first try to find init of sub class,
# if it is not found then it will call init of super class (from Left to Right).


class A:

    def __init__(self):
        print('INIt in A')

    def feature1(self):
        print("Feature-1-A is Working")

    def feature2(self):
        print("Feature-2 is Working")


class B:

    def __init__(self):

        print('INIt in B')

    def feature1(self):
        print("Feature-1-B is Working")

    def feature4(self):
        print("Feature-4 is Working")


class C(A, B):

    def __init__(self):
        super().__init__()
        print('INIt in C')

    def feat(self):
        super().feature2()
        #To represent super class we use super method

a1 = C()
# So, here as per rule it will call it's own init Method.

# Now after adding super().__init__(),
# It will call init method of Class A

# So, Here comes the concept of "Method Resolution Order(MRO)"

# Whenever you have this multiple inheritance, it will always start from left to Right.

a1.feature1()
# So this will call the feature1 of Class A as it always goes from Left to Right.

a1.feat()