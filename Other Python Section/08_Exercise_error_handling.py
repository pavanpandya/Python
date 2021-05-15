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
    finally:
        print("Okay, I'am Finally Done")
    print("Can you hear me?")

# Finally runs regardless at the end of everything.
# Though we use break to get out of the loop, Finally will still get executed.
# Print statement will not get executed as we have break the loop.
