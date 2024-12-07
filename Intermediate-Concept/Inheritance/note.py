#Inheritance: Create an electric car class that inherits form the car class and has an additional attribute battery size.
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def car_detail(self):
        print(f"car brand: {self.brand} and car model: {self.model}")

class ElectricCar(Car):
    def __init__(self, brand, model, batterysize):
        super().__init__(brand, model)
        self.batterysize = batterysize

obj = ElectricCar("Tesla", "model S", "90kwh")
print(obj.batterysize) #output: 90kwh
print(obj.car_detail()) #output: car brand: Tesla and car model: model S

#Instanceof Method in python
print(isinstance(obj, Car)) #true
print(isinstance(obj, ElectricCar)) #true

#Multiple Inheritance: Create two classes battery and engine and the electriccar class inherit from both, demonstrating multiple inheritance.
class One:
    def display(self):
        print("Hello sir, I am from one class")

class Two:
    def display_two(self):
        print("I am from class two")

class All_access_one(One, Two, Car):
    pass

obj = All_access_one("Tesla", "super-X")
obj.car_detail()
obj.display()
obj.display_two()

