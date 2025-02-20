fruit = ["apple", "banana", "orange", "pineapple"]
print(fruit)
print(fruit[0:3:2])
print(fruit[2])
fruit[2] = "apagado"
print(fruit)

for x in fruit:
    print(x, end=",")

fruit.append("orange")
print(fruit)

fruit.remove("banana")
print(fruit)

fruit.insert(0, "raksi")
print(fruit)

print(fruit[0])
print(fruit[1])

fruit.sort()
print(fruit)

result = [x**2 for x in range(10)]
print(result)

data = ["apple", "banana", "orange"]
result = [x for x in data]
print(result)

for index, value in enumerate(data):
    print(f"{index} of {value}")

list1 = [1,2,3]
list2 = ["a","b","c","d"]
for num, letter in zip(list1, list2):
    print(num, letter)

a = [1,2,3]
b = [2,4,5]
c = a+b
d = set(c)
e = list(d)
print(e)

a = [[1,2,3],[12,13,14]]
print(a[0][2])

b  = [[[12,13,14],[14,12,13]],[[10,11,12],[11,13,15]]]
print(b[0][0][1])

# Step 1: Take 25 inputs from the user
# numbers = []  # Empty list to store the numbers
# for _ in range(25):
#     num = int(input("Enter a number: "))
#     numbers.append(num)

# # Step 2: Filter even numbers
# even_numbers = [num for num in numbers if num % 2 == 0]

# # Step 3: Calculate the sum of even numbers
# even_sum = sum(even_numbers)

# # Step 4: Print the results
# print("The list of even numbers is:", even_numbers)
# print("The sum of the even numbers is:", even_sum)


age = 12
Print("you are eligible to vote") if age>18 else print("you are not eligible to vote")

person = {"name": "Anugraha tamang", 'age': 22, "location": "Kathmandu", }
print(person)

for key in person:
    print(key)

for value in person.values():
    print(value)

for key, value in person.items():
    print(f"{key} : {value}")

person["height"] = "5.4ft"
print(person)

person["name"] = "Jeewan tamang"
print(person)

print(person.get("name"))
print(person.pop("name"))
print(person)

del person["height"]
print(person)

result = {x: x**2 for x in range(4)}
print(result)

