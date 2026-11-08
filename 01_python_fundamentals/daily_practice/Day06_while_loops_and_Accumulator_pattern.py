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
