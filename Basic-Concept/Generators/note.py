def my_generator():
    for i in range(200):
        yield i

gen = my_generator()
print(next(gen)) #0
print(next(gen)) #1

for j in gen:
    print(j) # 1 dekhi 199 samma print hunxa
