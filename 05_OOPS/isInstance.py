# Is Instance - checks if an object is an instance of class or subclass.
# isinstance(object, classinfo) - returns True if object is an instance of classinfo or its subclass, otherwise False.

class Car :
    def __init__(self, brand, model, year) :
        self.brand = brand
        self.model = model
        self.year = year

class ElectricCar(Car): # ElectricCar is child class of Car class.
    def __init__(self, brand, model, year, battery_size) :
        super().__init__(brand, model, year)  # super() is used to call the init method of parent class. 
        self.battery_size = battery_size
    
my_tesla = ElectricCar("Tesla", "Model S", 2020, 100)

print(isinstance(my_tesla, ElectricCar)) # True
print(isinstance(my_tesla, Car)) # True
print(isinstance(my_tesla, object)) # True 
    
