amazon_cart = [
    'notebooks',
    'sunglasses',
    'toys',
    'grapes'
]

print(amazon_cart[0])  # Item at index 0 will be printed
print(amazon_cart)  # entire list will be printed

# List Slicing
print(amazon_cart[0:3:1])

# List are Mutable
amazon_cart[2] = 'laptop'
print(amazon_cart)  # entire list will be printed

# Important Note
# This will send/assign the copy of amazon_cart to new_cart
new_cart = amazon_cart[:]
# This will assign new_cart equal to amazon_cart (Will not send the copy)
new_cart = amazon_cart
