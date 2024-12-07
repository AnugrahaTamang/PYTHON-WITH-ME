#Polymorphism: Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but
#with the different behaviour.
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def add_sum(self, a, b):
        return a+b
    
class CarB(Car):
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)
        self.battery = battery
    def add_sum(self, a, b):
        return a + b

    def display(self):
        return f"My car brand is {self.brand} and my car model is {self.model} and my car battery is {self.battery}"

    
obj = CarB("BYD", "2020", "80kwh")
print(obj.display())
print(obj.add_sum(2,4)) #6

obj1 = Car("tesla", "2020")
print(obj.add_sum(12,2)) #14 

#multiple inheritance
class Father:
    def __init__(self):
        self.__name = "Ram"
    def display(self):
        print("Father Name:", self.__name)
class Mother:
    def __init__(self):
        self.__name = "Sita"
    def display(self):
        print("Mother Name: ", self.__name)

class Child(Father, Mother):
    def __init__(self):
        self.__name = "Hitesh"
        Father.__init__(self)
        Mother.__init__(self)
    def display(self):
        print("Name: ", self.__name)
        Father.display(self)
        Mother.display(self)

def main():
    C = Child()
    C.display()
main()

