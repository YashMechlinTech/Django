# Inheritence

class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def full_name(self):
        # return self.brand+" "+self.model
        return f"{self.brand} {self.model}"
    
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
       super ().__init__(brand,model) #accesing above __init__ method 
       self.battery_size=battery_size
    
mycar=Car("Tata","Safari")
print(mycar.full_name())

mytesla=ElectricCar("Tesla","Model S","85kWH")
print(mytesla.model)
print(mytesla.brand)
print(mytesla.battery_size)
print(mytesla.full_name())
