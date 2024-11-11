#opp: Object Oriented programming is non-procedural programming language. It is paradigm which is very effective to
# store the data. It's major feature  is class and object based code, Abstraction, Polymorphism, Inheritance.

#Class: Class is the blueprint or template for creating objects. It defines the properties(attributes) and behaviour(methods)
#that the objects created from the class will have.

#Object: Object is an instance of a class. When a class is defined, no memory is allocated until an object of
#that class is created. Each Object is unique and has its own set of attributes and behaviours as defined by the class


# Example of Class 
class Student:
    def __init__(self):  #method
        self.name = None #attribute
        self.age = None #attribute
    def input(self):
        self.name = str(input("Enter your name "))
        self.age = int(input("Enter your age "))
    def output(self):
        print(f"My name is {self.name} . I am {self.age} years old.")

#person1 is object
person1 = Student()
person1.input()
person1.output()

#Self: self keyword is like a this keyword. it's used to refer to the instance of the class itself, allowing you to access its attribute and methods.
#__init__(self) : It's is used to create a constructor

