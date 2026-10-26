name = "Roshan"
age = 21
print(name)
print(age)

name = "Roshan.R"
age = 20
print(f"{name}\n{age}") #prints the stored value in the variables in 2 different lines
rint(f"name\nage") #prints the words "name","age" in 2 different lines 

name = "Roshan"
age = 21
height = 5.9
is_student = True
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

name = "Roshan.R"
height = 5.10
age = 20 
print(f"my name is {name}\nI'm {height:.2f}\nAnd my age is{age}") #.2f to print upto 2 decimal points or it will print 5.1
# to use .2f , f-string in print statement is manditory 

age = 20
is_adult = age >= 18

if is_adult:
    print("You can watch the movie")
else:
    print("You cannot watch the movie") #use of boolean data type 


marks = int(input("Enter your marks: "))
if marks < 0 or marks > 100 :
    print("Invalid")
elif 0 <= marks < 40 :
    print("fail")
elif 40 <= marks <60 :
    print("C grade")
elif 60 <= marks < 75 :
    print("B grade")
elif 75 <= marks <= 100 :
    print("A grade")
