day = str(input("Enter your day: "))
match (day):
    case "sunday": 
        print("Hello sunday")
    case "monday":
        print("Hello monday")
    case __:
        print("Envalid day")
