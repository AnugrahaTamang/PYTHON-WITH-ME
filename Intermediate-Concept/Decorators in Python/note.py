#Decorators:  
#Problem One: Write a decorator that measures the time a function takes to execute.
import time
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start} time")
        return result
    return wrapper
@timer #This is also know as Decorators
def example_function(n):
    time.sleep(n)

example_function(3)

#Note: Decorator bhaneko function bhitra pni function banaunu ra teslai tehi function bhitra call garaunu ho.

#Problem two: Create a decorator to print the function name and the values of its argument every time the function is called.
def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(f"{k}={v}" for k, v in kwargs.items())
        print(f"calling: {func.__name__} with args {args_value} and kwargs value : {kwargs_value}")
        return func(*args, **kwargs)
    return wrapper

@debug
def Hello():
    print("Hello Anugraha")

Hello()

@debug
def display(name, age):
    print(f"my name is {name} and I am {age}")

display("Anugraha", 22)

@debug
def greet(name, greeting = "Hello"):
    print(f"{greeting}, {name}")
greet("Ramit")

#Problem Three: Implement a decorator that caches the return values of a function, so that when it's called 
# with the same argument, the cached value is returned instead of re-executing the function. 
def cache(func):
    cache_value = {}
    print(cache_value)
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result
    return wrapper
@cache
def long_running_function(a, b):
    time.sleep(4)
    return a+b
print(long_running_function(3, 5))
print(long_running_function(4, 6))

    


