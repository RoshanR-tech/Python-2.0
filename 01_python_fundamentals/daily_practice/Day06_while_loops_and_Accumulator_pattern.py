n = 1 
while n <= 10 :
    print(n)
    n += 1    #print numbers from 1-10 


n = 10 
while n >= 1 :
    print(n)
    n -= 1
     
print("Blast off!!!")    #print number from 10-1(reverse orde)


n = 1
total = 0 
while n<=10:
    total+=n 
    n+=1
    
print(total)  #Accumulator pattern 


n = 1
total = 0 
while n<=10 :
    if n%2==0:
        total+=n 
        
    n+=1 
print(total) #accumulate sum of even numbers from 1-10


n = 1 
while n<=15:
    if n == 7:
        n+=1
        continue
    
    elif n==12:
        break 
    print(n)
    n+=1    


n=1
while n<=20:
    if n%3==0:
        n+=1
        continue
    if n==17:
        break
    print(n)
    n+=1
print("Loop completed!!")


password = "maybeidk"
while True :
    pas = input("Enter your password: ")
    if pas == password :
        print("Login success.")
        break 
    
    else :
        print("Wrong password!!")    #password validation system 
        

se = 7 
while True :
    secret = int(input("enter your secret number: "))
    if secret == se :
        print("Congratulations! You guessed it.")
        break 
    
        
    else:
        if secret < 7:
            print("Too low.")
        if secret > 7 :
            print("Too high.")
        print("Wrong guess! Try again.")


while True :
    print("-----Menu-----")
    print("1.Addition.")
    print("2.Subtraction.")
    print("3.multiplication.")
    print("4.Division.")
    print("5.exit")
    
    op = int(input("Select an option: "))
    
    if op==1 :
        a=int(input("enter a number: "))
        b=int(input("enter a number: "))
        print(a+b)
        
    elif op==2:
        a=int(input("enter a number: "))
        b=int(input("enter a number: "))
        print(a-b)
        
    elif op==3:
        a=int(input("enter a number: "))
        b=int(input("enter a number: "))
        print(a*b)
        
    elif op==4:
        a=int(input("enter a number: "))
        b=int(input("enter a number: "))
        if b==0 :
            print("Cannot be divide by 0")
        else:
            print(a/b)
        
    elif op==5:
        print("Exit done.")
        break
    
        
    else :
        print("invalid input. ")  #menu driven program 


n = 1
total = 0
while n<=10:
    total+=n
    n+=1
    
print(total) #Accumulator pattern 


total = 0 
count = 0 
while count<5:
    n = int(input("Enter a number: "))
    total += n
    count += 1 
    
print("total=",total)
avg = (total/count)
print(f"Average = {avg:.2f}")  #counter + accumulators


total = 0 
count = 0 
even_count = 0 
while count < 5 :
    n = int(input("Enter your number: "))
    if n%2==0 :
        total+=n 
        even_count+=1
        
    count+=1
print(f"Total is {total}")
if even_count > 0 :
    avg = (total/even_count)
    print(avg)
else :
    print("No even numbers")   #counter and accumulator for even numbers only


total = 0 
positive_num = 0
negative_num = 0
zeros = 0
count = 0 
while count < 10 :
    n = int(input("Enter your number: "))
    if n > 0 :
        total+=n
        positive_num+=1
    elif n < 0 :
        negative_num+=1
    elif n == 0 :
        zeros+=1
    count+=1
print("sum of positive numbers is ",total)
print("total positive numbers: ",positive_num)
print("total negative numbers: ",negative_num)
print("total number of zeros: ",zeros)        #Positive, Negative and Zero Counter


big = None 
second_big = None 
count = 0 
while count < 10 :
    n = int(input("Enter a number: "))
    if count == 0 :
        big = n 
    elif n > big :
        second_big = big
        big = n 
    elif n!= big and (second_big is None or n < second_big):
        second_big = n 
    count+=1
print(big)
if second_big != None :
    print(second_big)
else :
    print("There is no second largest number")         #second largest number from 10 numbers


small = None 
second_small = None 
count = 0 
while count < 10 :
    n = int(input("Enter a number: "))
    if count == 0 :
        small = n 
    elif n < small :
        second_small = small 
        small = n 
    elif n!= small and (second_small is None or n < second_small):
        second_small = n 
    count+=1
print(small)
if second_small != None :
    print(second_small)
else :
    print("There is no second smaller number")     #second smallest number from 10 numbers


total = 0 
passed = 0 
fail = 0 
count = 0 
big = None 
small = None 
while count < 10 :
    n = int(input("Enter your marks : "))
    if n>35 :
        passed+=1 
    elif n < 35 :
        fail +=1
    total+=n 


    if count == 0 :
        big = n
        small = n 
    elif n > big :
        big = n 
    elif n < small :
        small = n 
    count+=1
print("Total marks: ",total)
avg = (total/count)
print("the average is : ",avg)
print("Total number of students who passed: ",passed)
print("Total number of students who failed: ",fail)
print("highest marks: ",big)
print("lowest marks: ",small)             #student marks analysis program


count = 0
es = 0 
os = 0 
en = 0
on = 0 
while count < 10 :
    n = int(input("Enter a number : "))
    if n%2==0 :
        es+=n
        en+=1
    else :
        os+=n
        on+=1
    count+=1
print("Even sum: ",es)
print("Odd sum : ",os)
print("Even numbers :" ,en)
print("Odd numbers :" ,on)      #sum and count of even and odd numbers from 10 numbers
