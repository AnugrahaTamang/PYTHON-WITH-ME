# Collection of Character called string.
name = "Anugraha Tamang"
print(name)
print(name[2]) #u

#slicing
print(name[:]) #output: Anugraha Tamang
print(name[0:]) #output: Anugraha Tamang

print(name[3:4]) #g
print(name[: -1]) #g

numvalue = "12345678"
print(numvalue[0:7:2]) # 2 number skip Output: 1357
print(numvalue[1:7:2]) # ouput: 246

#Some String Method
data = "Hello sir, How are you?"
print(data.upper())
print(data.lower())
data = "    Hello G    "
print(data.strip())

fruit = "Apple, Banana, Orange, pineapple"
print(fruit.split(', '))  # output: ['Apple', 'Banana', 'Orange', 'pineapple'] It converts array
fruit_type = "Apple"
quantity = 2
order = "I am ordered {} kg of {}"
print(order.format(quantity, fruit_type))  #ouptut: I am ordered 2 kg of Apple

print(" - ".join(fruit))

data = "Apple juice \"best\" for the health."
print(data) #output: Apple juice "best" for the health.

data = "Apple is \nGood for Health"
print(data)
''' output: Apple is 
Good for Health'''
data = r"Apple is \nGood for Health"
print(data) #ouptut: Apple is \nGood for Health

