#Immutable Datatype: Immutable datatype is unchangeable data. 
a = "Hello world"
print(type(a)) #string
a = 12
print(type(a)) #int
a = 12.121
print(type(a))  #float
a = 1212j
print(type(a))  #complex
print(a)
a = True
print(type(a)) #bool
a = (12,13,"anugrah")
print(a)
print(type(a)) #tuple

#This is frozent set datatype
frozen = frozenset([1,2,3,4,5])
another_frozen = frozenset([2,3,4,5,6,6,7])
print(f"Union of {frozen | another_frozen} ") #output: Union of frozenset({1, 2, 3, 4, 5, 6, 7}) 
print(f"Intersection of {frozen & another_frozen}") #output: Intersection of frozenset({2, 3, 4, 5})
print(f"Difference of {frozen - another_frozen}") #output: Difference of frozenset({1})

#This is the byte datatype example
byte_data = bytes([66, 67, 68, 67])
print(f"Byte value of {byte_data}") #output : Byte value of b'BCDC'

#Askue value find method
for byte in b"ABC":
    print(byte)

# Converting a string to bytes with encoding
string_data = "Hello"
byte_string = string_data.encode('utf-8')  # Encoding as UTF-8
print("Encoded bytes:", byte_string)  # Output: b'Hello'

# Accessing individual bytes (immutable)
print("First byte:", byte_string[0])  # Output: 72 (ASCII code for 'H')

# Decoding bytes back to string
decoded_string = byte_string.decode('utf-8')
print("Decoded string:", decoded_string)  # Output: Hello


#This is about the mutable data type
list_one = [13,33,34]
print(type(list_one)) #list

dict_one = {"name": "ramit", "age": 33}
print(dict_one)
print(type(dict_one))  #dict

set_one = {2,3,"ramit"}
print(type(set_one)) #set

# Creating a bytearray
my_bytearray = bytearray([65, 66, 67])
print("Original Bytearray:", my_bytearray)  # Output: bytearray(b'ABC')

# Modifying an element
my_bytearray[1] = 68
print("After Modification:", my_bytearray)  # Output: bytearray(b'ADC')
