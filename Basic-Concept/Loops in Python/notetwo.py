#Iteration tool and comprehension
mylist = [1,2,3,4,5]
one = iter(mylist)
print(one.__next__()) #output: 1
print(one) #memory location: <list_iterator object at 0x0000019BFF655A20>
print(one.__next__()) #output: 2
print(one.__next__()) #output: 3
print(one.__next__()) #output: 4
print(one.__next__()) #output: 5
print(one.__next__())


