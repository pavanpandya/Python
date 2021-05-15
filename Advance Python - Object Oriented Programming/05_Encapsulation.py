# 4 Pillars of OOP:
# 1. Encapsulation: Encapsulation in Python is the process of wrapping up variables and methods into a single entity.In programming, a class is an example that wraps all the variables and methods defined inside it.
# 2. Abstraction: Abstraction in Python is the process of hiding the real implementation of an application from the user and emphasizing only on usage of it.
# 3. Inheritance:  It is the process of creating a class that can derive or inherit the properties and methods from another class(parent/base).
# 4. Polymorphism: Polymorphism means the ability to take various forms.

# Encapsulation:

# Encapsulation is a process of protecting the data and functionality of a class in a single unit, called an object.
# This mechanism is often used to protect the data of an object from other objects.
# It’s one of the fundamental principles in any programming language that supports object-oriented programming.
# We can protect the variables in the class by marking them as private. We need to add two underscores as a prefix to make a variable private.
# Once we make a variable as private, we can’t access them directly from the objects of that class.
# Now, let’s see how to create private variables:

# eg:
from abc import abstractmethod, ABC


class House:

    def __init__(self, wallDynamic):
        self.__wall = wallDynamic

# In the above example, wall is a private variable.
# Once a variable is declared as private, the only way to access those variables is through name mangling.
# In the name mangling process, an identifier with two leading underscores and one trailing underscore is
# textually replaced with _classname__identifier , where class-name is the name of the current class and identifier is the private variable.


house = House(1)

# Using name mangling to access private variables
print(house._House__wall)  # OutPut - 1

# To implement proper encapsulation in Python, we need to use setters and getters, as shown below:


class House2:

    def setWall(self, dynamicWall):
        self.wall = dynamicWall

    def getWall(self):
        print(self.wall)


# Abstraction:

# Abstraction in OOP is a process of hiding the real implementation of the method by only showing a method signature.
# In Python, we can achieve abstraction using ABC(abstraction class) or abstract method.
# ABC is a class from the abc module in Python.
# If we extend any class with ABC and include any abstraction methods,
# then the classes inherited from this class will have to mandatorily implement those abstract methods.
# When we annotate any method with an abstractmethod keyword, then it is an abstract method in Python(it won’t have any method implementation).
# If the parent class has abstractmethod and not inherited from an abstract class, then it is optional to implement the abstractmethod .


class Vehicle(ABC):
    def __init__(self, speed, year):
        self.speed = speed
        self.year = year

    def start(self):
        print("Starting engine")

    def stop(self):
        print("Stopping engine")

    @abstractmethod
    def drive(self):
        pass


class Car(Vehicle):
    def __init__(self, canClimbMountains, speed, year):
        Vehicle.__init__(self, speed, year)
        self.canClimbMountains = canClimbMountains

    def drive(self):
        print("Car is in drive mode")


# Here, Vehicle is a parent inherited from ABC class. It has an abstraction method drive.
# Car is another class that is inherited from Vehicle, so it had to implement the drive method.
