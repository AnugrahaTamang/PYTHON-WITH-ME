#This is about the shallow and deep copy in python.

#Shallow copy: where shallow copy does affect the original value. it's like a mutable 
#shallow copy Example:
import copy
original_list = [[1, 2, 3], [4, 5, 6]]
print(original_list)
print(original_list[0][2]) #output: 3
print(original_list[0][0]) #output: 1
shallow_copy_list = copy.copy(original_list)  #This is the shallow copy
print(shallow_copy_list) #output : [[1, 2, 3], [4, 5, 6]]
shallow_copy_list[0][0] = "Ramit"
print(f"Original list of {original_list}") # output:Original list of [['Ramit', 2, 3], [4, 5, 6]]
print(f"shallow copy of : {shallow_copy_list}") #output: shallow copy of : [['Ramit', 2, 3], [4, 5, 6]]

#Deep Copy: where deep copy doesn't affect the original value.It's like a immutable
#Deep Copy Example:
original_value = [[2,4,6],[3,5,7]]
print(original_value)
deep_copy_value = copy.deepcopy(original_value)
deep_copy_value[0][0] = "Jeewan"
print(f"Original of value: {original_value}")
print(f"Deep Copy of value: {deep_copy_value}")
