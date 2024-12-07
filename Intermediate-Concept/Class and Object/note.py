# Basic class and Object: create a car class with attributes like brand and model. Then create an instance of this class.
'''class Car:
    def __init__(self, brand, model): #self: it's like a this keyword. communication channel between obj and class.
        self.brand = brand
        self.model = model

my_car_one = Car("BYD", "2024")
print(my_car_one.brand)
print(my_car_one.model)

my_car_two = Car("Tesla", "2026")
print(my_car_two.brand)
print(my_car_two.model)'''

# Class Method and self: Add a method to the car class that displays the full name of the car(brand and model)
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def car_detail(self):
        print(f"My car brand is {self.brand} and model is {self.model}")

obj = Car("BYD", 2024)
print(obj.car_detail())



