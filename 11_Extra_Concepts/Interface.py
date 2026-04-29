# No concept of Interface in Python
# We can achieve the concept of interface using abstract classes in Python.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod   # Declaring an abstract method
    def show(self):   # No Implementation, must define in child class
        pass
    
    @abstractmethod
    def Disp(self):    # another abstract method
        pass           # Cannot create object of shape.
    
class Square(Shape):
    def Disp(self):   # Implements the one abstract method.
        pass
        
class Circle(Square):  # Inherits the class, circle is abstract class because it has one abstract method.
    def show(self):    # implements the missing method show() from shape class.
        print("This is a Circle")
        
c = Circle()   # Object creation of circle class. 
c.show() 

# If circle implements all abstract methods ? 
## Yes - allow object creation  &&  NO - raise error.