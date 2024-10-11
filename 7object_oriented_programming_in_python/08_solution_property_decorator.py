# Using the property decorator to make the "model" variable read only.


class Car:
    total_car_made = 0 

    def __init__(self, brand, model):
        self.__brand = brand  # private variable
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

    @property  # property method make the attirbute read only. property method also stops the overriding.
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

# safari.model="City" # giving error on : overiding the model attribute which was allowed initially

print(safari.getmodel)
