basket = [1, 2, 3, 4, 5]

print(len(basket))

# Methods

# Here this will not assign the values of basket in the new list called 'new_basket'
# instead it will implement the changes in the basket list
new_basket = basket.append(100)
print(basket)
print(new_basket)

# This will print none as "basket.insert(0, 0)" doesn't return anything
# print(basket.insert(0, 0))
basket.insert(0, 0)
print(basket)

basket.extend([101])
# basket.extend('good')
# this will add good at the end of the list like this [ 'g', 'o', 'o', 'd']
print(basket)

# NOTE: Here the difference between extend and append is extend iterates the argument in it and then add the element one by one at the end of the list
# where as append directly adds the element at the end of the list.

basket.pop()
# Here pop will delete the last element in the list and if we provide the index as  argument  then it will delete the element at that particular index
# newlist = basket.pop(0)
# Here .pop will return the value it deleted at index 0 and if we print newlist it will give the output as follow
# print(newlist)
print(basket)

basket.remove(100)
# Here remove will delete 100 from the list if it exist else it will print none
print(basket)

basket.clear()
# Here Clear will empty the list
print(basket)

container = ["a", "b", "c", "d", "e", "d"]
container.sort()
# Here .sort method will not return any value
print(container)

print(sorted(container))
# Here sorted is build in function and will create a copy for container
# sorted function works as :
# new_container = container[:]
# or
# new_container = container.copy()
# new_container.sort()
# print(new_container)

print("d" in container)
# By using we get output in form of true or false.
# Here as d is present in the container it will return true.
# This is a good way to check if particular character is present in the list or not without any error in the program.

container.reverse()
print(container)

# container can also be reversed by using list slicing
# print(container[::-1])

sentence = " "
new_sentence = sentence.join(['hi', 'my', 'name', 'is', 'Pavan'])
print(new_sentence)

# The above code can also be written as:
new_sentence = ' '.join(['hi', 'my', 'name', 'is', 'Pavan'])
print(new_sentence)
