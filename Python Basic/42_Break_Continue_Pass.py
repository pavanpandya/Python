# Break: Used when you want the loop to end(break it's flow)
j = 0
while j < 50:
    print(j)
    # j = j + 1
    j += 1  # Shorthand
    break

# Continue: Whatever happens when you hit this line, continue on to the top of the enclosing loop.
Somelist = [1, 2, 3]
for k in Somelist:
    continue
    # Here Continue will work till the condition becomes false and loop ends.
    # print(k)
    # This will not get printed as it comes after continue.

# Pass: Used when you at first don't know what to write and want to leave it blank
Something = [1, 2, 3]
for i in Something:
    # thinking what to do
    # If you leave it this way without writing anything, Python Interpreter will throw an error, so to deal with it we can use:
    pass  # It says pass to the next line
