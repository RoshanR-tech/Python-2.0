for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()  #basic star triangle pattern


for i in range(5,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()  #Reverse star triangle pattern


for i in range(1,6):
    for j in range(5-i):
        print(" ",end=" ") 
        
    for j in range(i):
        print("*",end=" ")
    print()      #Right aligned star triangle pattern


for i in range(1,6):
    for j in range(5-i):
        print(" ",end=" ")
    
    for j in range(2*i-1):
        print("*",end=" ")
    print()     #pyramid pattern 


for i in range(1,6):
    for j in range(5-i):
        print(" ",end=" ")
        
    for j in range(2*i-1):
        print("*",end=" ")
    
    print()

for i in range(5,0,-1):
    for j in range(5-i):
        print(" ",end=" ")
        
    for j in range(2*i-1):
        print("*",end=" ")
    print()       #diamond pattern
        
   
for i in range(5,0,-1):
    for j in range(5-i):
        print(" ",end=" ")
        
    for j in range(2*i-1):
        print("*",end=" ")
    print()
        
for i in range(2,6):
    for j in range(5-i):
        print(" ",end=" ")
        
    for j in range(2*i-1):
        print("*",end=" ")
    
    print()    #Hour glass pattern 


for i in range(1,6):
    for j in range(i):
        val=(i*(i-1))//2+j+1
        print(val,end=" ")
    print()      #Floyd's Triangle (Consecutive Numbers):
