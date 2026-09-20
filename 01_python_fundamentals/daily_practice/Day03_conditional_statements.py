age = int(input("Enter your age:"))  #boolean data type example 
is_eligible = age>=18
if is_eligible :
    print("you can watch the movie.")
else :
    print("you cannot watch this movie.")


age = 16
print(age >= 18)
print(age < 18)
print(age == 16)  #only prints true or false (boolean)


print(7 > 3)
print(4 < 2)
print(5 == 5)
print(8 != 8)  #only prints true or false (boolean)


age = int(input("Enter your age: "))
if age >= 18:
    print(f"you are {age} years old")


num = int(input("Enter a number: "))
if num > 0 :
    print("Number is positive.")
else :
    print("Number is not positive")


num = int(input("Enter a number: "))
if num > 0 :
    print("Positive.")
elif num < 0 :
    print("Negative")
else :
    print("zero")   #Basic conditions 
    

age = int(input("Enter your age: "))
if age >= 18 :
    has_id = input("Do you have an ID: ")
    if has_id == "yes":
        print("You can enter.")
    else :
        print("ID required.")
else :
    print("You are under aged.")
    

marks = int(input("Enter your marks: "))
if marks >= 40 :
    assignment = input("completed assignment ?: ")
    if assignment == 'yes':
        print("you are eligible for exam: ")
    else :
        print("you are not eligible")
else :
    print("you are not eligible")
    
    

marks = int(input("Enter your marks: "))
if marks >= 0 and marks < 40 :
    print("Fail")
elif marks >= 40 and marks < 50 :
    print("C Grade")
elif marks >= 50 and marks < 75 :
    print("B Grade")
elif marks >= 75 and marks <= 100 :
    print("A Grade")
else :
    print("invalid")


age = int(input("Enter your age: "))
marks = int(input("Enter your marks: "))
if age >= 18 and marks >= 50 :
    print("Eligible")
else :
    print("Not eligible")   #AND operator 


age = int(input("Enter your age: "))
marks = int(input("Enter your marks: "))
if age >= 18 or marks >= 50 :
    print("Eligible")
else :
    print("Not eligible")    #OR operator


login_username = "Roshan.R"
login_password = "Hello@123"
username = input("Enter your username: ")
password = input("Enter your password: ")
if username == login_username and password == login_password :
    print("Login successful")
else :
    print("Invalid credentials")


num = int(input("Enter a number: "))
if num == 0 :
    print("Zero")
else :
    print("Non Zero")
