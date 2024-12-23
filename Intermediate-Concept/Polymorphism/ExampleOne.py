#This is about the polymorphism
class Car:
    def __init__(self, name, color):
        self.name = name 
        self.color = color
    
    def get_output(self):
        print(f"My car name is {self.name}. My car color is {self.color}")

class ElectricCar(Car):
    def __init__(self, name, color, model):
        super().__init__(name, color)
        self.model = model

    def get_output(self):
        print(f"My car name is {self.name}. My car color is {self.color}")

objone = ElectricCar("Tesla", "red", "2024")
objtwo = Car("BYD", "white")
objone.get_output()
objtwo.get_output()