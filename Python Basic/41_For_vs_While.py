my_list = [1, 2, 3]

for i in my_list:
    print(i)

j = 0
while j < len(my_list):
    print(my_list[j])
    j += 1

# for Simple Rules and Iterating Objects for Loops are great.

# But You are not sure how long you need to do looping then at that time while loops are great.
# Example:
while True:
    response = input('Say Something: ')
    if(response == 'bye'):
        break
