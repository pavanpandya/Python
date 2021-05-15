# Infinite Loop
# i = 0
# while i < 50:
# print(i)

i = 0
while i < 50:
    print(i)
    # i = i + 1
    i += 1  # Shorthand
else:
    print("Done with all the work")
    # Here else is Optional.
    # Also, if it successfully runs, it indicates that while loop have finish the work perfectly

j = 0
while j < 50:
    print(j)
    # j = j + 1
    j += 1  # Shorthand
    break
else:
    print("Done with all the work")
    # Here else will not get executed because while loop has not completed his work 100%. While loop is forced to stop using break.

# Thus, Successfull execution of else ensures us that the while loop has completed it's 100% work.
