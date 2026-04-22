class Car :
    def __init__(self, brand, model, year) :
        self.brand = brand
        self.model = model
        self.year = year
    
car1 = Car("Hyundai", "i10", 2021)
print(car1.brand)  
print(car1.model)

car2 = Car("Kia", "Seltos", 2022)
print(car2.brand)
print(car2.year)

#car1 and car2 are two objects with its own attributes. 
# car1 and car2 are two instances of the Car class.
# self is a reference to the current instance of the class. It is used to access the attributes and methods of the class.
# brand, model, year = parameters of init method. 


# In short 
# Class is blueprint of objects 
# Attributes = properties  
# Instance = Objects
