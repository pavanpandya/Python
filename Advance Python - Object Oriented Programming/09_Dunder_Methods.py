# Dunder methods or Magic methods.

class Toy():

    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'Yoyo',
            'has_pets': False
        }

    def __str__(self):
        return f'{self.color}'

    def __len__(self):
        return 5

    def __call__(self):
        return('Yess!!')

    def __getitem__(self, i):
        return self.my_dict[i]


action_figure = Toy('red', 0)
print(action_figure.__str__())
print(str(action_figure))
# Both the print function will give us the same output.
# Output: <__main__.Toy object at 0x016C51F0>

# Now Modifying the __str__() dunder method.
print(action_figure.__str__())
print(str(action_figure))

# We will modify the dunder method in some cases where we want our class to behave in certain manner.

print(len(action_figure))

my_list = [1, 2, 3]
print(len(my_list))
# Here len method will behave normally except the action_figure as it's class __len__() method behave differently.

print(action_figure())
# Here call dunder method will bahave differently.

print(action_figure['name'])
