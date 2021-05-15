# Clean Code

# def is_even(num):
#     if(num % 2 == 0):
#         return True
#     else:
#         return False


# Now the above Function can also be Defined as:
# def is_even(num):
#     if(num % 2 == 0):
#         return True
#     return False

# Now the above Function can also be Defined as:
def is_even(num):
    return num % 2 == 0


print(is_even(13))
