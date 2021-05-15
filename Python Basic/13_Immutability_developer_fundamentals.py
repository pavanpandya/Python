a = '01234567'
# a = '0  1  2  3  4  5  6  7'
#      0  1  2  3  4  5  6  7  for the reference
#     -8 -7 -6 -5 -4 -3 -2 -1  for the reference

# Immutable = Cannot be changed

a = '100'  # Here we can reassign the whole String ( Will not throw any error)

# Here this will throw an error because strings are immutable i.e You can not change it's particular element once assigned.
# a[0] = '8'
# Here we can add 8 to string but we cannot replace 0 with 8.
a = a + '8'  # This will add 8 at the end of the string.

print(a)
