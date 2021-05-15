# List Unpacking

a, b, c = [1, 2, 3]
e, f, g = 1, 2, 3
print(a, b, c)
print(e, f, g)

p, q, r, *other = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(p)
print(q)
print(r)
print(other)

p, q, r, *other, s = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Here writing s after other will return the last value of the list

print(p)
print(q)
print(r)
print(other)
print(s)
