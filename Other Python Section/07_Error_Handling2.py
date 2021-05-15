# Error Handling:

def sum(num1, num2):
    try:
        return num1 + num2
    except TypeError as err:
        print(f'Please Enter Numbers, {err}')
    # except (TypeError, ZeroDivisionError,..) as err:
    #     print(f'Please Enter Numbers, {err}')
    # We can wrap multiple errors in one like this.


print(sum('1', 2))
