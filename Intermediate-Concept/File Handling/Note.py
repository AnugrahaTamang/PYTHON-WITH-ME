#file handling : It's used to handle the data into file format.
#create the file method
f = open("myfile.txt", "w")
print(f.write("Hello My name is Ramit Tamang. I am from Dhading Nepal. I am 22 years old"))
# f.close()
f = open("myfile.txt", "r")
print(f.readline())
f = open("myfile.txt", "a")
print(f.write(" Hello Ramit"))

import os
os.remove("myfile.txt")