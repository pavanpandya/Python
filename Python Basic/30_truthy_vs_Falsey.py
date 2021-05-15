is_old = 'hello'
is_licenced = 5

# Now python converts them into boolean (truthy or falsey) values for if condition i.e:
# is_old = bool('hello')
# is_licenced = bool(5)
# print(bool('hello')) --> True
# print(bool(5)) --> True
# print(bool('')) --> False
# print(bool(0)) --> False

if is_old and is_licenced:
    print("You can drive!")
else:
    print("you cannot drive")

print("Check-2 Completed")


# All the value are truthy except:

# None
# False
# 0
# 0.0
# decimal(0)
# Fraction(0,1)
# [] - empty list
# {} - empty dict
# () - empty tuple
# '' - empty str
# set() - empty set
