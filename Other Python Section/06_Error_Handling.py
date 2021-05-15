# Error Handling:

while True:
    try:
        age = int(input('What is your age: '))
        print(age)
    except:
        print('Please enter a number')
    # The above code means try the code and if there is any error run except.
    else:
        print('Thank You')
        break

# If there is any error then instead of some pre_written error, msg(print in above case) written in except will get printed.

# If there are multiple diff error:

while True:
    try:
        age = int(input('What is your age: '))
        print(age)
    except ValueError:
        print('Please Enter a number')
    except ZeroDivisionError:
        print("You can't Enter Zero")
    else:
        print('Thank You')
        break
