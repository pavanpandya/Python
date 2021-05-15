# eg: 5 + 6
# Here 5 and 6 are operands and + is operator.

a = 5
b = 6

print(a+b)

# When you say a + b behind the scene int.__add__(a, b) is called.
print(int.__add__(a, b))

c = '5'
d = '6'

print(c+d)

# When you say c + d behind the scene str.__add__(c, d) is called.
print(str.__add__(c, d))

# The moment you say a - b then .__sub__(a, b) is called
# The moment you say a * b then .__mul__(a, b) is called
# The moment you say a / b then .__div__(a, b) is called
# The moment you say a > b then .__gt__(a, b) is called
# The moment you say a < b then .__lt__(a, b) is called
# The moment you say a >= b then .__ge__(a, b) is called
# The moment you say a <= b then .__le__(a, b) is called
# These Methods are called as Magic Methods.


class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        # Adding m1 of student 1 and student 2
        m1 = self.m1 + other.m1
        # Adding m2 of student 1 and student 2
        m2 = self.m2 + other.m2
        s3 = Student(m1, m2)
        return s3

    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        # Here r1 and r2 are not objects they are simple integer variables.
        if(r1 > r2):
            return True

    def __str__(self):
        # return self.m1, self.m2
        # The above line will generate an error:
        # TypeError: __str__ returned non-string (type tuple)
        # So we have convert it into string.
        return '{} {}'.format(self.m1, self.m2)


s1 = Student(58, 69)
s2 = Student(68, 79)

# This will throw an error because we have not defined add method.
# print(s1 + s2)

# This 's1 + s2' gets converted into 'Student.__add__(s1, s2)'.
s3 = s1 + s2

print(s3.m1)
print(s3.m2)

if s1 > s2:
    print("S1 Wins")
else:
    print("S2 Wins")

f = 5
print(f)
# when we type print(f), behind the scene print(f.__str__()) is called.

# when we type print(s3), behind the scene print(s3.__str__()) is called.
# But here it will print the address of s3.
# As we want values we have to overwrite this method.
print(s3)
# Now it will print the values.
