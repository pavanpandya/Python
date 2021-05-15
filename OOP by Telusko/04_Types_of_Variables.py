# Variables are of two types:
# 1 - Instance Variable.
# 2 - Class(Static) Variable.

class Car:

    wheels = 3  # Class Variable.

    def __init__(self):
        self.company = "BMW"
        self.mileage = 10
        # Here these two variable are called as Instance Variable.


c1 = Car()
c2 = Car()

c2.mileage = 8
# So, Here when we change the value, the change will only reflect in c2 object as mileage is an Instance variable.

Car.wheels = 4
# So, Here when we change the value, the change will reflect to every object as wheel is an Class variable.

print(c1.company, c1.mileage, c1.wheels)
print(c2.company, c2.mileage, c2.wheels)

# Namespace- Namespace is an area where you create and store objects/Variable.
# They are of 2 types: 1. Class Namespace and 2. Object/Instance Namespace.
# So wheels belong to Class Namespace and Company, Mileage belongs to Object/Instance Namespace.
