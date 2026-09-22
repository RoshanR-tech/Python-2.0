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
