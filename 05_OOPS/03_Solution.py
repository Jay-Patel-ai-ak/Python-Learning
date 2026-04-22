# Inheritance - Reusing attributes and methods of parent class in child class.
# super() is used to call the init method of parent class.

class Car :
    def __init__(self, brand, model, year) :   #init is method of class car. 
        self.__brand = brand
        self.model = model
        self.year = year
    
    # Getter Method
    def get_brand(self) :  # getter method to access private attribute brand.
        return self.__brand
    
    def full_name(self) :   # full_name is method of class Car.
        return f"{self.__brand} {self.model}"
    
class ElectricCar(Car): # ElectricCar is child class of Car class.
    def __init__(self, brand, model, year, battery_size) :
        super().__init__(brand, model, year)  # super() is used to call the init method of parent class. 
        self.battery_size = battery_size
    
class SuperCar(Car): # SuperCar is child class of Car class. 
    def __init__(self, brand, model, year, top_speed) :
        super().__init__(brand, model, year)  # super() is used to call the init method of parent class. 
        self.top_speed = top_speed

# Parent Attributes - brand, model, year
# Child Attributes - battery_size, top_speed
 
top_speed_car = SuperCar("Bugatti", "Chiron", 2021, 261)
print(top_speed_car.full_name())
    
my_tesla = ElectricCar("Tesla", "Model S", 2020, 100)
print(my_tesla.full_name())


# Acccess Specifiers / Access Modifiers - Public, Private, Protected
# Public - can be accessed from anywhere.
# Private - can be accessed only within the class.
# Protected - can be accessed within the class and its subclasses.

# Encapsulation - Wrapping data and methods into a single unit. Restricting direct access to protect data. 


print(top_speed_car.model) # access from everywhere
# print(my_tesla.brand) # access from everywhere  

print(my_tesla.get_brand()) # access private attribute using getter method.   
print(top_speed_car._Car__brand) # access private attribute using name mangling. Not recommended.