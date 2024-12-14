# You will able to know conditional statement with given problem and solution.
#Question 1: Classify a person's age group: child(<13), Teenager(13-19), Adult(20-59), Senior(60+).
'''age = int(input("Enter your age: "))
if(age<13):
    print("You are child")
elif(age>13 and age<19):
    print("you are teenager")
elif(age>20 and age<59):
    print("you are adult")
else:
    print("You are senior")'''

#Question 2: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on wednesday.
'''age = int(input("Enter your age: "))
day = str(input("Enter your Day: "))
price = 12 if age>=18 else 8 
if(age):
    if(day == "wednesday"):
        price -= 2
        print("Ticket price is $",price)
    else:
        print("Ticket price is $",price)'''

#Question 3: Assign a letter grade based on a students score: A(90-100), B(80-90), c(70-90), d(60-69), f(below 60)
# grade = int(input("Enter your date: "))
'''if (grade>=90 and grade<100):
    print("You're grade is A")
elif (grade>=80 and grade<90):
    print("You are grade is B")
elif (grade>=70 and grade<80):
    print("you are grade is C")
elif (grade>=60 and grade<70):
    print("you are grade is D")
elif (grade<60):
    print("you are grade is not goood")
else:
    print("Enter your accurate data")'''

#match in python
age = 12
match age:
    case 10:
        print("you are smaller")
    case 12:
        print("you are equal")
    case _:
        print(" i am default")

        





