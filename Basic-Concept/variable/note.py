# vriable is container which is used to store different type of data value.
a = 12
b = 13
print(a+b)
a = "Anugraha Tamang"
print(a)

#Two types of variable in python .
#1. Mutable: which is changeable.
#2. Immutable : which is unchangeable.

print(2+4j) #Complex variable

a = True
print(a)

fruit = "apple", "banana", "orange"
# it's like a destructure way
apple, banana, orange = fruit
print(apple)
print(orange)

# Global variable
name = "Anugraha Tamang"
def myfun():
    print(f"My name is {name}")

myfun()
print(name)

# Local scope variable
def myfun():
    name = "Ramit Tamang"
    print(f"My name is {name}")
myfun()
print(name) #Anugraha Tamang