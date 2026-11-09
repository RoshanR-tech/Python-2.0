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
