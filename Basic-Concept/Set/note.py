# Set store the unique data in python. Example of set
basket = {"orange", "apple", "orange", "banana", "pineapple"}
print(basket)
num = 12

a = set('abcdefgha')
b = set('fgabjkl')
print(a-b) #output: {'e', 'd', 'h', 'c'}

valueone = {1,3,5,7}
valuetwo = {0, 2, 4, 6}
print(valueone.union(valuetwo))
print(valueone.intersection(valuetwo))
print(valuetwo.difference(valueone))

nameone = {"anugraha", "ramit", "jewan", "mika", "seema", "amisha"}
nametwo = {"ramit", "yahoshu", "milan", "suman", "saran", "jewan"}
print(nameone.intersection(nametwo)) # output: {'jewan', 'ramit'}
print(nameone.difference(nametwo)) #output: {'mika', 'seema', 'amisha', 'anugraha'}
print(nameone.union(nametwo)) #output: {'ramit', 'suman', 'seema', 'yahoshu', 'jewan', 'mika', 'anugraha', 'milan', 'saran', 'amisha'}
print(nameone.symmetric_difference(nametwo)) #output: {'saran', 'anugraha', 'seema', 'suman', 'milan', 'amisha', 'mika', 'yahoshu'}
print(nameone)
nameone.add("Tej")
print(nameone)
nameone.remove("anugraha")
print(nameone)