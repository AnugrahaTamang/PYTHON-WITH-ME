class Animal:
    def __init__(self, name):
        self.name = name
    
    def show(self):
        print(f"my name is {self.name}")

class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)
    
    def showone(self):
        print(f"Animal name is {self.name}")

class GoldenRetriver(Dog):
    def __init__(self, name):
        Dog.__init__(self, name)
     
    def showtwo(self):
        print(f" Here the {self.name}")


objone = GoldenRetriver("ramit")
objone.showtwo()