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
        print(" ",end=" ") #space for right alignment
        
    for j in range(i):
        print("*",end=" ")
    print()      #Right aligned star triangle pattern
