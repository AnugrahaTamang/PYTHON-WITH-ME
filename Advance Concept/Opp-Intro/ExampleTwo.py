class Calculations:
    def __init__(self):
        pass
    def input(self):
        self.num1 = int(input("Enter your first Number: "))
        self.num2 = int(input("Enter your second Number: "))
        self.num3 = int(input("Enter your third Number: "))
    def Addittion(self):
        print(f"The value of addition num1 + num2 + num3 =  {self.num1 + self.num2 + self.num3}")
    def Subtraction(self):
        print(f"num1 - num2 = {self.num1 - self.num2}")
    def Area(self):
        print(f"area of l * b = {self.num1 * self.num2}")
    def Volume(self):
        print(f"The value of Volume l*b*h = {self.num1 * self.num2 * self.num3}")

obj = Calculations()
obj.input()
obj.Addittion()
obj.Subtraction()
obj.Area()
obj.Volume()