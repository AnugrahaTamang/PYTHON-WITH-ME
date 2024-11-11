#Operator: Operator is Symbol. Which is used to perform operation into operand/variables. 
# 1. Arithmetic Operator
print(12 +12)
print(13-12)
print(13/2)
print(13//2)
print(13%3)
print(3**3)

#2. Assignment Operator
x = 1
print(x)
x += 2
print(x)
x -= 2
print(x)
x *= 3
print(x)
x **= 12
print(x)
x /= 12
print(x)
x //= 12
print(x)
x%= 12
print(x)

#3. Comparison operator
print(12 == 13) #false
print(4 != 2) #true
print(5>2)   #true
print(3<4)  #true
print(4>=3)  #true
print(12<=12) #true


# 4. Logical Operator: and, or, not
print("This is ", (5>2) and (3<6)) #true
print((5>3) or (3>6)) #true
print(not(5>3)) #false

#5. Bitwise Operator: &, `, ^, ~, <<, >>
a = 5 & 3 
print(a)
b = 5^3
print(b)
c = ~5
print(c)
d = 5<<1
print(d)
e = 5>>2
print(e)

#6. Membership Operator : in, not in
print("a" in "apple") #true
print("b" not in "apple") #true

#7. Identify Operator: is, is not
x = 12
y = 12
print(x is y) #true
x = 13
print(x is not y) #true

# 8. Ternary Operator
x = 13
result = "Even" if x % 2 == 0 else "Odd"
print(result)  #odd

# 9. Operator Overloading
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

# Using the overloaded `+` operator
p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2
print(p3)  # Output: (4, 6)
