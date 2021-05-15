# Short Circuiting

is_friend = True
is_user = True

print(is_friend and is_user)

if is_friend and is_user:
    print("Best Friends")
# This only runs when both the conditions are true.
# Here Interpreter will check the first condition if it is false it does not care what is the remaining condition,
# it will directly execute the block.

if is_friend or is_user:
    print("Best Friends")
# This will run when any of the one condition is true.
# Here Interpreter will check the first condition if it is true it does not care what is the remaining condition,
# it will directly execute the block.
