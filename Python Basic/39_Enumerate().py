# Enumerate is very useful if you need index counter of the item you are looping through

for item in enumerate('PavanPandya'):
    print(item)

for index, item in enumerate('PavanPandya'):
    print(index, item)

for index, item in enumerate([1, 2, 3]):
    print(index, item)

for index, item in enumerate(list(range(100))):
    if item == 50:
        print(f'Index of 50 is: {index}')
