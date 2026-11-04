for i in range(1,6):
    for j in range(1,i+1):
        print(i,end=" ")
    print()     #same value 


for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()      #different value


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


for i in range(1,6):
    for j in range(i):
        letter = chr(65+j)
        print(letter,end=" ")
    print()      #Alphabet pattern 


n=5
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end=" ")
        else :
            print(" ",end=" ")
    print() #Hollow pattern 
