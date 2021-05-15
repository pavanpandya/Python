class A:
    num = 10


class B(A):
    pass


class C(A):

    num = 1


class D(B, C):
    pass


print(D.num)
print(D.mro())
# This will show you the order.
# It tells that first it will check D, then B, then C, then A and then object class.
