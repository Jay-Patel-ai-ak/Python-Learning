class Car :
    def __init__(self, brand, model, year) :   #init is method of class car. 
        self.brand = brand
        self.model = model
        self.year = year

class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_size) :
        super().__init__(brand, model,)  # super() is used to call the init method of parent class. 
        self.battery_size = battery_size


class Battery :
    def battery_info(self) :
        return "Battery is there in car"
        
class Engine:
    def engine_info(self) :
        return "Engine is there in car"

class ElectricCarTwo(Battery, Engine, Car) :
    pass


new_car = ElectricCarTwo("Tesla", "Model S", 2020)
print(new_car.engine_info())
print(new_car.battery_info())


# Multiple Inhertitance -- A class can inherit from multiple classes.
