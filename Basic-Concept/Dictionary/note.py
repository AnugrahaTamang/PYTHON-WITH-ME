#Dictionary: Collection of Key value pairs.
data = {"name": "Ramit", "age": 22, "location": "Kathmandu"}
print(data)
print(data.get("name")) #Ramit

#looping with dictionary
for key, Value in data.items():
    print(key, Value)
if "name" in data:
    print("I am here")

# Add the data
data["Hobbies"] = "Volleyball"
print(data)
data.pop("name")
print(data)
del data["Hobbies"]
print(data)
dataone = data.copy()
print(dataone)
data["Hobbies"] = "Football"
print(data)
print(dataone)

store = {
    "Person1": {"Name": "Anugraha", "location": "ktm", "age": 22},
    "Person2": {"Name": "Ramit", "Location": "Dhading", "age": 23},
}
print(store)
print(store["Person1"]["Name"]) #Anugraha
print(store["Person2"]["Location"]) #Dhading

squared_num = {x: x**2 for x in range(10)}
print(squared_num)
cube_num = {x: x**3 for x in range(5)}
print(cube_num)

keys = ["masala", "ginger", "lemon"]
print(keys)
default_value = "Delicious"
print(dict.fromkeys(keys, keys))
'''
{'masala': ['masala', 'ginger', 'lemon'], 'ginger': ['masala', 'ginger', 'lemon'], 'lemon': ['masala', 'ginger', 'lemon']}
'''
print(dict.fromkeys(keys, default_value)) #output: {'masala': 'Delicious', 'ginger': 'Delicious', 'lemon': 'Delicious'}

store = dict(sape=4139, guido=4127, jack=4098)
print(store) #output: {'sape': 4139, 'guido': 4127, 'jack': 4098}