# Static method in class doesn't require the self and can be called without an object.


class Car:
    total_car_made = 0  # initially the total car which are made is zero .

    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total_car_made = Car.total_car_made + 1

    def full_name(self):
        return f"{self.__brand} {self.model}"

    def get_brand(self):
        return self.__brand

    def fuel_type(self):
        return "Petrol Or Diesel"

    @staticmethod
    def genreal_description():  # adding the static method to make sure no object can access the function no object required to call the function.
        return "Cars are means of the Transport. "


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
print(Car.genreal_description())
print(ElectricCar.genreal_description())
