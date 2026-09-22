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
