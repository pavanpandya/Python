# Functions always returns, if return is absent in function definition then it will return none.
# Return automatically exits the function

def sum(num1, num2):
    return num1 + num2


print(sum(4, 5))


# Nested Function
def sum2(num1, num2):
    def another_func(n1, n2):
        return n1 + n2
    return another_func(num1, num2)


total = sum2(10, 5)
print(total)
