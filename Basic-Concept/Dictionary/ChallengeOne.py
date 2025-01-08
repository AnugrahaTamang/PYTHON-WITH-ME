person = {"name": "ramit", "age": 22, "location": "Kathamandu"}
# print(person)
# # add 
# person["Hobbies"] = "volleyballl"
# print(person)

# #update
# person["Hobbies"] = "football"
# print(person)
# print(person.get("name"))

# # remove
# print(person.pop("name"))
# print(person)
# print(person.popitem())

print(person.keys)
print(person.values)

for key, values in person.items():
    print(f"{key}: {values}")

