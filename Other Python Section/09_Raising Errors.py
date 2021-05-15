while True:
    try:
        age = int(input('What is your age: '))
        print(age)
        raise ValueError("Enter a Number")
    except ZeroDivisionError:
        print("You can't Enter Zero")
    else:
        print('Thank You')
        break
