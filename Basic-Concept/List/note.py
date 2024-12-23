#List: Collection of Similar type of data.
name = ["ramit", "jeewan", "vandai"]
print(name)
print(type(name)) # list
#for the slicing in python
print(name[0:2])
name[1] = "Binod"
print(name)
name[1:2] = ["sam", "Rabin"]
print(name) #Output: ['ramit', 'sam', 'Rabin', 'vandai']

tea_varities = ["masala", "ginger", "Icetead"]
for tea in tea_varities:
    print(tea, end="-") #output: masala-ginger-Icetead-

#Some List Method in Python
#(append, pop, remove, insert)
name = ["ramit", True, 12, "vandai"]
print(name)
print(name.pop())
print(name)
print(name.append("Jeewan Tamang"))
print(name)
print(name.remove(12))
print(name)
print(name.insert(1, "bj"))
print(name)

# Square and Cube in List 
squared_num = [x ** 2 for x in range(10)]
print(squared_num)#output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
cube_num = [x ** 3 for x in range(10)]
print(cube_num) #output: [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]


 