#In the python two type of data. Mutable and Immutable .
# Mutable: The value of an object can be changed in place after it is created. Examples: lists, dictionaries, sets, bytearrays.
# Immutable types: The value of an object cannot be modified after it is created. Instead, any changes result in the creation of a new object. Examples: integers, boolean, floats, strings, tuples, frozensets, and complex numbers.

#Immutable Example
x = 12
print(id(x))  #memory address of x 3529531880
x = 13
print(id(x))  # memory address of x 14073529
x += 12
print(x)
print(id(x))  #memory address of x 140735295319224


#Mutable example:
a = [1, 2, 3]
print(a)
print(id(a)) #memory address of a :1765705060928
a.append(12)
print(a)
print(id(a)) #memory address of a: 1765705060928
