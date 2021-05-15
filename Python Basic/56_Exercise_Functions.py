def Highest_Even_Number(li):
    evens = []
    for item in li:
        if(item % 2 == 0):
            evens.append(item)
    max = 0
    for i in evens:
        if(i > max):
            max = i
    return max
    # By using Max Function.
    # return max(evens)


my_List = [10, 2, 3, 4, 8, 11]
print(Highest_Even_Number(my_List))
