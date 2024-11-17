#Inheritance : New class from Old class.
class A:
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location

    def getOutput(self):
        print(f"My name is {self.name}. I am {self.age} years old. I am from {self.location}")

class B(A):
    def __init__(self, name, age, location):
        A.__init__(self, name, age, location)
class C(B):
    def __init__(self, name, age, location):
        B.__init__(self, name, age, location)


def main():
    objectone = B("prasun", 22, "Gorkha")
    objectTwo = C("ramesh", 23, "ktm")
    objectone.getOutput()
    objectTwo.getOutput()
main()
