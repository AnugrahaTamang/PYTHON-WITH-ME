class Car:
    def __init__(self, name, model, price):
        self.name = name
        self.model = model
        self.price = price
    def output(self):
        print(f"My car name is {self.name} Model {self.model} and price is {self.price}")

def main():
    objone = Car("Tesla", 2024, 200000)
    objone.output()

if __name__ == "__main__":
    main()