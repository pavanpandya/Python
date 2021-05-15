# Logical Operators:
# >, <, >=, <=, ==, !=
# and, or, not

print(4 > 5)
print(4 >= 5)
print(4 < 5)
print(4 <= 5)
print(4 == 5)
print(4 != 5)

print('a' > 'b')
print('a' > 'A')

print(1 < 2 < 3 < 4)

print(not(True))

# Exercise

is_magician = False
is_expert = True

if is_magician and is_expert:
    print("You are a master magician")
elif is_magician and not is_expert:
    print("You are an Average magician")
elif not is_magician:
    print("You are not magician")
