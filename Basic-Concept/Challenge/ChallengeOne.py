x = 2
y = 3
print("x=",x)
print("Value of ", x, "+", x , "is", (x+x))
print((x+y)==(y+x) )  #Output: true
print((x+y),"=", (y+x)) #output: 5 = 5

# rating = int(input("Enter your interger rating between 1 and 10 : "))
# if rating>=0 and rating<10:
#     print(rating)

x = "apple"
print(x in 'apple')
print(x not in "a")
y =12
print(x is y)
z = y
print(z is y)
print(z is not y)

result = 13
onepoint = "even num" if result%2 == 0 else "odd"
print(onepoint)

y = 13
print("Even num") if y%2 ==0 else print("odd num")

name = "ramit tamang from dhading Nepal. He is the the Nepali Boy."
print(name)
# print(name.replace("ramit", "jeewan"))
# data = str(input("Enter your data"))
# print(name.join(data))
print(name.upper())
print(name.lower())

data = "ram bahadur tamang"
dataone = data.encode('utf-8')
print(dataone.decode('utf-8'))
print(dataone[::-1])

valone = "ramit tamang is hiro"
print(valone.split())
data = ["anugraha tamang", "ramit tamang", "Jeewan tamang"]
print(" ".join(data)) #convert to string

