# Class Method and Self 

# Self is not keyword, Its parameter of init method. 
# Used to access the attributes and methods of class. 
# Self is reference to current instance of class. 
# Self is placeholder for the current object.

class Car :
    def __init__(self, brand, model, year) :   #init is method of class car. 
        self.brand = brand
        self.model = model
        self.year = year
    
    def full_name(self) :   # full_name is method of class Car.
        return f"{self.brand} {self.model}"
    
car1 = Car("Hyundai", "i10", 2021)
print(car1.full_name())  

car2 = Car("Kia", "Seltos", 2022)
print(car2.full_name())

# Methods are functions defined inside a class.  