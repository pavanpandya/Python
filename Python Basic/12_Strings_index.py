a = '01234567'
# a = '0  1  2  3  4  5  6  7'
#      0  1  2  3  4  5  6  7  for the reference
#     -8 -7 -6 -5 -4 -3 -2 -1  for the reference
print(a[7])
# print(a[7]) --> This will print the element at index 7

# [Start: Stop: Stepover]  ----> Syntax
# [Start: Stop: Stepover]  ----> Also know as String Slicing

# here, It will start a from 0 (including it) and will stop at 4 (without including it).
print(a[0:4])
# Mechanism: Start from 0 and stop as soon as you see 4

# In order to grab full string
print(a[0:8])

# Step Over
print(a[0:8:1])  # By default
print(a[0:8:2])  # It will skip every 2nd element.


# Extra
# If we leave it blank, By Default it will take default value i.e print(a[0:lenth_of_String:1])
print(a[::])

# Printing the last element of String
print(a[-1])

# Printing the String in Reverse Order
print(a[::-1])  # It means start from 0 and stop at 8 and stepover from -1.

# Return the string without any whitespace at the beginning or the end.
txt = " Hello World "
x = txt.strip()

# Replace the character H with J.
txt = "Hello World"
txt = txt.replace("H", "J")
