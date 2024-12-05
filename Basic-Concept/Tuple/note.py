#Tuple: Collection of data. List is mutable and Tuple is immutable
data = ("ramit","suman","jewan","anu", 12, True)
print(data[1]) #output: suman
print(data)
print(data[3: 5]) #output: ('anu', 12)
dataone = (1,2,3)
datatwo = (4,5,6)
datathree = dataone + datatwo
print(datathree)
print(dataone.count(2)) #output: 1

datastore = (1,23, 43, 34, 54)
(a, b, c, d, e) = datastore
print(b) #output: 23

