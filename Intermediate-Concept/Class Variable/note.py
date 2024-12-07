#Class variable: add a class variable to car that keeps track of the number of cars created.
class Car:
    total_car = 1
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Car.total_car += 1

one = Car("tesla", "2020")
two = Car("Byd", "2022")
three = Car("toyota", "1010")
print(Car.total_car) #output: 4
#Note: it's used to check how many car objects is created.


            