# Class Variable


class Car:
    total_car_made = 0  # initially the total car which are made is zero .

    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total_car_made =Car.total_car_made+1 ##class variable to keep record of all the classes that are made under the object Car.

    def full_name(self):
        # return self.brand+" "+self.model
        return f"{self.__brand} {self.model}"

    def get_brand(self):
        return self.__brand

    def fuel_type(self):
        return "Petrol Or Diesel"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"


safari = Car("Tata", "Safari")
safari = Car("Tata2", "Safari2")
mytesla = ElectricCar("Tesla", "Model S", "85kWH")


print(Car.total_car_made)
