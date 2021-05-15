# Method Overriding:
# It Simply means we have two methods with same name and same number of parameters or arguments (But not in same class).

class A:

    def show(self):
        print("In A Show")


class B(A):

    def show(self):
        print("In B Show")


s1 = B()
s1.show()
