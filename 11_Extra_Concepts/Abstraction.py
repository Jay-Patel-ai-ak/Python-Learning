# Python by default does not support abstraction, but we can achieve it using classes and methods.
# We have module -- abc module which provides the infrastructure for defining abstract base classes (ABCs) in Python.

# What is abstract class?
# An abstract class is a class that cannot be instantiated and is meant to be subclassed.
# The method which has declaration but not implementation is called abstract method. Defined in class with @abstractmethod decorator.

# Abstract class will have one abstract method. 

from abc import ABC, abstractmethod   # abc = abstract base class & ABC

class Car (ABC):
    def show(self):
        print("This is a Car")
    @abstractmethod
    def speed(self):
        pass
    
class BMW(Car):
    def speed(self):
        print("BMW can run at 200 km/h")
    
class Lamborghini(Car):
    def speed(self):
        print("Lamborghini can run at 300 km/h")

# c = Car()  # This will raise an error because we cannot instantiate an abstract class.
b = BMW()
b.show()  # This will work because show() is a concrete method.
b.speed() # This will work because speed() is implemented in BMW class.

l = Lamborghini()
l.show() 
l.speed()