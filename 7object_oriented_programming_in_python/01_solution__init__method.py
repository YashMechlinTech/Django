class Car:
    brand = "Toyota"
    model = "Supra"

    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

my_car = Car("Lambhorghini","Aventador")
print(my_car.brand)
print(my_car.model)
 