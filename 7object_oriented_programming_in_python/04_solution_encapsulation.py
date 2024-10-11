# Encapsulation

class Car:
    def __init__(self,brand,model):
        self.__brand=brand #using underscore two times to make it private attribute(variable) could only be accessed by the getter functions . 
        self.model=model
    def full_name(self):
        # return self.brand+" "+self.model
        return f"{self.__brand} {self.model}"
    def get_brand(self):
        return self.__brand
    
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
       super ().__init__(brand,model) #accesing above __init__ method 
       self.battery_size=battery_size
    
mycar=Car("Tata","Safari")
print(mycar.full_name())
print("get brand method: ",mycar.get_brand())

mytesla=ElectricCar("Tesla","Model S","85kWH")
print(mytesla.model)
# print(mytesla.brand) This line will throw error because the brand variable is protected with __ (double underscore "which is used to make the variables private")
print(mytesla.battery_size)
print(mytesla.full_name())
