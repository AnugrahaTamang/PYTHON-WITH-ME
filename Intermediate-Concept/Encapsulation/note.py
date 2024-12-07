#Encapsulation: modify the car class to encapsulate the brand attribute, making it private, and provide a getter method for it.
class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
    def get_brand(self):
        return self.__brand + " ! "
    def car_detail(self):
        print(f"car brand: {self.__brand} and car model: {self.model}")

class ElectricCar(Car):
    def __init__(self, brand, model, batterysize):
        super().__init__(brand, model)
        self.batterysize = batterysize

obj = ElectricCar("Tesla", "model S", "90kwh")
print(obj.batterysize) #output: 90kwh
print(obj.car_detail()) #output: car brand: Tesla and car model: model S

# print(obj.__brand) #not accessible
print(obj.get_brand()) #output: Tesla !  Note: it's called the encapsulation



