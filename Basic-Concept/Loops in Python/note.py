#Loop: How many times program terminated is called loop.
#Question 1: Count positive numbers
'''numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
positive_count_num = 0
for num in numbers:
    if num>0:
        positive_count_num = positive_count_num + 1
print("Positive count num :", positive_count_num)'''

#Question 2: Sum of even number
'''number = int(input("enter your number: "))
sumvalue = 0
for i in range(1, number+1):
    if i%2 == 0:
        sumvalue += 1
print("Even number total: ",sumvalue)'''

#Question 3: print the multiplication table for a given number up to 10, but skip the fifth iteration.
'''number = int(input("Enter your number: "))
for i in range(1, 11):
    if i == 5:
        continue
    print(number, '*', i, '=', number * i)'''

#Question 4: Reverse a string using loop
'''input_str = str(input("Enter your string: "))
reverse_str = ""
for char in input_str:
    reverse_str = char + reverse_str
print(reverse_str)'''

#Question 5: Given a string, find the first non-repeated character.
'''input_str = str(input("Enter your string: "))
for char in input_str:
    print(char)
    if input_str.count(char) == 1:
        print("non repeated str", char)
        break'''

#Question 6: Compute the factorial of a number using a while loop.
'''number = int(input("Enter your number: "))
factorial = 1
while number>0:
    factorial = factorial * number
    number -= 1
print("factorial : ", factorial)'''

#Question 7: keep asking the user for input until they enter a number between 1 and 10.
'''while True:
    number = int(input("Enter your number between 1 to 10: "))
    if 1 <= number <=10:
        print("Thanks")
    else:
        print("Try again")'''

#Question 8: check if a number is prime or not.
number = int(input("Enter your number: "))
is_prime = True
if number > 1:
    for num in range(2, number):
        if (number % num) == 0:
            is_prime = False
            break

print(is_prime)

#Question 9: check if all elements in a list are unique. if a duplicate is found, exit the loop and print the duplicate.
'''items = ["apple", "banana", "apple", "orange", "banana"]
unique_items = set()

for item in items:
    if item in unique_items:
        print("Duplicate: ", item)
        break
    unique_items.add(item)'''

#Question 10: Implement an exponential  backoff stratey that doubles the wait time betweeen retries, starting from 1 seconds, but stops after 5 retries.
'''import time
wait_time = 1
max_retries = 5
attempts = 0
while attempts < max_retries:
    print("attempts", attempts +1, " wait time", wait_time)
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1'''



    

