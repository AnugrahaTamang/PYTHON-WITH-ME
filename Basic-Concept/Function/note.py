# Question 1: write a function multiply that multiplies two numbers, but can also accept and multiply string.
'''def myfun(a, b):
    return a * b
result = myfun(2, 3)
print(result) #ouput: 6
result = myfun(2, 'a')
print(result) #output: aa'''

#Lamda function in python
cube = lambda x: x**3
print(cube(2)) #output: 8


#Example one in lamda
details = lambda name, age, location: f"my name is {name}. I am {age} years old. I am from {location}"
print(details("Anugraha", 22, "kathmandu")) #output: my name is Anugraha. I am 22 years old. I am from kathmandu

#args in python (power of args parameter)
def sum_all(*args):
    print(args)
    return sum(args)
print(sum_all(1, 3)) #output: 8
print(sum_all(1,2,3,4)) #output: 10
print(sum_all(3,4,5,6)) #output: 18

#kwargs in python 
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f" {key} : {value}")
print_kwargs(name="anugraha", power = "super ")
print_kwargs(name="ramit", power="superhiro")

#yield operator in python . Note: yield चहि return ko sattama use garinxa.
def even_generator(limit):
    for i in range(2, limit +1, 2):
        yield i
    
for num in even_generator(10):
    print(num, end=" ") #output: 2 4 6 8 10
for num in even_generator(20):
    print(num, end=" ") #output: 2 4 6 8 10 12 14 16 18 20 

#Last Question in function: Recursive function, create a recursive function to calculate the factorial of a number
def factorial(n):
    if n ==0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5)) #1120
print(factorial(4)) #24









