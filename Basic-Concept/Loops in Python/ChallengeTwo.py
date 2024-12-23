# Write a program to find the factorial of a given number using a loop.
'''num = int(input("Enter your number: "))
fac = 1
for i in range(1, num + 1):
    fac = fac * i
print(f"Factorial number of {num} :  {fac}")'''

# Count the number of digits in an integer provided by the user.
# num = int(input("Enter your Number: "))
# count = 0
# while (num>0):
#     num = num // 10
#     count = count + 1
# print("Number of digit: ", count)


# Write a program to calculate the sum of the digits of a number (e.g., 123 → 1+2+3 = 6).
# num = int(input("Enter your Number: "))
# sumof_digits = 0
# while (num>0):
#     sumof_digits = sumof_digits + num % 10
#     num = num // 10
# print("sum of the digits: ", sumof_digits)


#Prime Number Checker
num = int(input("Enter your number: "))
for i in range(2, num):
    if (num%i == 0):
        print("prime Number: ", i)
    