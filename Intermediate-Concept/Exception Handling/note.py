#Exception Handling
try:
    a = int(input("Enter your first Number:"))
    b = int(input("Enter your second Number:"))
    c = a/b
except Exception as e:
    print("An error occured:",e)

else:
    print("Operation successful")

finally:
    print("Finally successful")