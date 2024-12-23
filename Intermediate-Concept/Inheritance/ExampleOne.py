class Car:
    def __init__(self, name, model):
        self.name = name 
        self.model = model 
    def output(self):
        print(f" Car name: {self.name} Car model: {self.model}")

class ElectricCar(Car):
    def __init__(self, name, model, price):
        super().__init__(name, model)
        self.price = price
    
    def output(self):
        super().output()
        print(f"Car name: {self.name} Car model: {self.model} Car price: {self.price}")

objone = Car("Tesla", 2024)
objone.output()

objtwo = ElectricCar("Toyota", 2025, 1230432)
objtwo.output()