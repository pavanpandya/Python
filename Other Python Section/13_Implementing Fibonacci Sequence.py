# My approach at first
# total_num = int(input('Enter n:'))

# num1 = 0
# num2 = 1
# print(num1)
# print(num2)

# for _ in range(total_num-1):
#     num3 = num1 + num2
#     print(num3)
#     num1 = num2
#     num2 = num3


# Better Approach
def fib(number):
    num1 = 0
    num2 = 1

    for _ in range(number):
        yield num1
        temp = num1
        num1 = num2
        num2 = temp + num2


number = int(input('Enter n:'))
for x in fib(number+1):
    print(x)
