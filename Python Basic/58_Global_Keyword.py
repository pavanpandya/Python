total = 0
total2 = 0


def count():
    global total
    total += 1
    return total


# Dependency Injection - Better Way
def count2(total2):
    total2 += 1
    return total2


# Using Global Keyword
count()
count()
print(count())
# Using Dependency Injection
print(count2(count2(count2(total2))))
# Here we have detech the Dependency of count2 function on total2. So, instead of using that global keyword we can still do our work.
