# Polymorphism

class Car:
    def __init__(self,brand,model):
        self.__brand=brand
        self.model=model
    def full_name(self):
        # return self.brand+" "+self.model
        return f"{self.__brand} {self.model}"
    def get_brand(self):
        return self.__brand
    def fuel_type(self): # Polymorphism
        return "Petrol Or Diesel"
    
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
       super ().__init__(brand,model) 
       self.battery_size=battery_size 
    def fuel_type(self):  # Polymorphism
        return "Electric Charge"
    
safari=Car("Tata","Safari")

mytesla=ElectricCar("Tesla","Model S","85kWH")

print(safari.fuel_type())
print(mytesla.fuel_type())

