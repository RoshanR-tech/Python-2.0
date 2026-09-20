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
    


    
    
