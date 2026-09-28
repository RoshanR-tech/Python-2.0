age = int(input("Enter your age: "))
if age >= 18 :
    ID = 6769
    valid_ID = int(input("enter your valid ID: "))
    if valid_ID == ID :
        print("Valid ID")
    else :
        print("Invalid ID")
else :
    print("under age")


age = int(input("Enter your age: "))
if age >= 18 :
    ID = 6769
    valid_ID = input("enter your valid ID: ")
    if valid_ID == ID :
        print("Valid ID")
    else :
        print("Invalid ID")
else :
    print("under age")     #>enter 6769 , it says invalid . because ID is an integer data type and "input()" will take in the data as string .
                           #>so we use "int(input())" to convert it into integer data type.
                           #>or ID's data type should be converted into a string by using '' or "".


un = "Roshan.R"
up = "Rossi@123"
user_name = input("Enter Your User Name: ")
if user_name == un :
    password = input("Enter your Password: ")
    if password == up :
        print("Login successful")
    else :
        print("Wrong password")
else :
    print("User name does not exist")


marks = int(input("Enter your score: "))
if marks >= 0 and marks <= 100:
    if marks>=0 and marks<40:
        print("Fail")
    if marks>=40 and marks<60 :
        print("D grade")
    elif marks>= 60 and marks<75:
        print("c grade")
    elif marks>= 75 and marks <90:
        print("B grade")
    elif marks >= 90 and marks<=100 :
        print("A grade")
else :
    print("Invalid")
