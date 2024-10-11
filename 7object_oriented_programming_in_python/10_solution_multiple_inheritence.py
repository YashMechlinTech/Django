# Demonstrate Multiple Inheritence : Create two class Battery and Engine and let the class Electriccar2 inherting properties from it showing the multiple inheritence property.


class Car:
    total_car_made = 0 

    def __init__(self, brand, model):
        self.__brand = brand  
        self.__model = model
        Car.total_car_made = Car.total_car_made + 1

    def full_name(self):
        return f"{self.__brand} {self.__model}"

    def get_brand(self):
        return self.__brand

    def fuel_type(self):
        return "Petrol Or Diesel"

    @staticmethod
    def genreal_description():
        return "Cars are means of the Transport. "

    @property 
    def getmodel(self):
        return self.__model


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"

    @staticmethod
    def genreal_description():
        return "Electric cars are charged by electricity and are good means of transport and good value for money"



safari = Car("Tata", "Safari")
mytesla = ElectricCar("Tesla", "Model S", "85kWH")

# print(isinstance(mytesla,Car))  
# print(isinstance(mytesla,ElectricCar))


#performing the multiple inheritence in python. 
class Battery:
    def battery_info(self):
        return "this is the battery"
class Engine:
    def engine_info(self):
        return "this is the engine"

class ElectricCar2(Battery,Engine,Car):
    pass


new_tesla=ElectricCar2("Tesla","Model x ")

print(new_tesla.battery_info())
print(new_tesla.engine_info())