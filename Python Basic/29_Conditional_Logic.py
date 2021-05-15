is_old = True
is_licenced = True

if is_old:
    print("You are old enough to drive")
    # The spacing you see before print is called "indentation" in python
    # and it helps interpreter to understand that yes this is one block or part of if.
elif is_licenced:
    print("You can drive now!")
else:
    print("you cannot drive")

print("Check Completed")

if is_old and is_licenced:
    print("You can drive!")
else:
    print("you cannot drive")

print("Check-2 Completed")
