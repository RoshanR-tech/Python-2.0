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
