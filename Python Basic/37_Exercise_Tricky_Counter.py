# Counter
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# MY ANSWER - I Thought we have to count the no. of items but we have to sum them and then print the sum

# Code to count the Number of items.
c = 0
for count in my_list:
    c += 1

print(c)

# Code to get the sum.
c = 0
for sum in my_list:
    c += sum

print(c)

# ANSWER
counter = 0
for item in my_list:
    counter += item

print(counter)
