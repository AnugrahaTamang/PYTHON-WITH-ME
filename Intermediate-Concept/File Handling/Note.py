#File Handling
file = open("youtube.txt") #it's used to open already made file
file = open("youtube.txt", "w") # It's used to make file as well as write mode

'''
file = open("youtube.txt", "w")
try:
    file.write("Anugraha Tamang")
finally:
    file.close()
''' 
# OR
'''
with open('youtube.txt', 'w') as file:
    file.write("Hello Anugraha Gomja")
'''