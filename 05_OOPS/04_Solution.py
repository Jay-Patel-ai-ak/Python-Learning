# Polymorphism : Poly - many , morphism - forms.
# Make multiple function --> same name but different parameters.
# Same method name with different behaviour.

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def full_name(self):
        return f"{self.brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol"
    
class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_size):
        super().__init__(brand, model, year)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric"
    
car1 = Car("Hyundai", "i10", 2021)
print(car1.full_name())
print(car1.fuel_type())

my_tesla = ElectricCar("Tesla", "Model S", 2020, 100)
print(my_tesla.full_name())
print(my_tesla.fuel_type())

