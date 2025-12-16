# Create a Car class with brand, model, and a drive() method.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        print(f"The {self.brand} {self.model} is driving now. Vroom vroom!")

# Testing the class
my_car = Car("Tesla", "Model S")
my_car.drive()

old_car = Car("Toyota", "Corolla")
old_car.drive()
