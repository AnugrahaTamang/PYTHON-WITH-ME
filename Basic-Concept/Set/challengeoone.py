a = {2,4,6,8,10,12,3}
b = {2,4,5}
c = {1,2,3,5,10,20,30}

print("value of a: ",a)
print("value of b: ", b)
print("value of c: ",c)

#union of a b c
print(a | b | c)

#intersection of a b c
print(a & b & c)

#symmetric differen
print(a-b)
print(a^b)


a = {1,2,3,4,5,6}
b = {1,2,3,4,5}
c = {10,20}
print(b.issubset(a))
print(a.issuperset(b))
print(a.isdisjoint(c))