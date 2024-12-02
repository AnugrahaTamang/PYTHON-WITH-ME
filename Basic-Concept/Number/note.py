# This is about the Number in python.

# Converting Number one type to another type. 
print(int(12.22)) #it;s the float value in python but it converts into integer. 

# Type of Number: int, float, complex, binary, decimal, octal, Hexadecimal

print(type(12)) #int
print(type(12.22)) #float
print(type((2 + 1j) * 2)) #complex
print(type(10000038838938j)) # it's also known as complex number in python.
 

# Math library
import math
print(math.floor(12.12))
print(math.trunc(13.33))


#Random library
import random
print(random.random())
print(random.randint(1, 10))
l1 = ["mango", "banana", "apple", "orange"]
print(random.choice(l1)) # कहिले बानाना त कहिले स्याउ कहिले सुन्तला त कहिले आप
print(random.shuffle(l1)) # None

print(0o20) #octal
print(0xff) #hexadecimal
print(0b101) #binary

print(oct(16)) # 0o20
print(bin(5)) #0b101
print(hex(255)) #0xff

# Number Conversion 
print(int('64', 8)) #decimal to octal conversion output: 52
print(int('12', 16)) #decimal to hexadecimal conversion output: 18
print(int('1000', 2)) #binary to decimal conversion output: 8

# why we need to import decimal 
# -> Answer is given problem.
print(0.1 + 0.1 + 0.1) # output: 0.30000000000000004 but expected output: 0.3
print((0.1 + 0.1 + 0.1) - 0.3) # output: 5.551115123125783e-17 but expected output: 0.0

from decimal import Decimal
print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1')) # output: 0.3
print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')) # output: 0.0


#fraction number
from fractions import Fraction
myfra = Fraction(2, 5)
print(myfra)
print(type(myfra))  #fractions
