#Static Method: Add a static method to the car class that returns a general description of a car.
class Car:
    def __init__(self):
        print("Hello sir")
    
    @staticmethod
    def display():
        return "This is about the static method."


obj = Car() #ouput: Hello sir
# print(obj.display()) Note: object can not access the static method
print(Car.display()) #This is about the static method.

#Note: static method syntax is @staticmethod before function. static method can access only Class Name.
#Note: @staticmethod it's also known as decorators in python.

