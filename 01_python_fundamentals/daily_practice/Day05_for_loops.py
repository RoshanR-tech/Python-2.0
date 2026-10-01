for i in range (1,6):
    print("pyhton")
    
    
for i in range (1,11):
    print(i)


for i in range (1,11):
    if i%2==0 :
        print(i)     #Even numbers from 1 to 10 without step function 


for i in range (2,11,2):
    print(i)   #Even numbers from 1 to 10 with step function


for i in range (10,0,-1):
    print(i)  #Reverse counting from 10 to 1


for i in range (10,0,-1):
    print(i, end=" ") #Reverse counting from 10 to 1 in a single line with space in between


for i in range(2,21):
    if i%2==0:
        print(i)   #Even numbers from 2 to 20 with loop


for i in range(2,21,2):
    print(i)   #Even numbers from 2 to 20 with step function


for i in range(1,71):
    if i % 7 == 0:
        print(i)


for i in range (1,11):
    print(i*i)   #square of numbers from 1 to 10   


for i in range(1,11):
    if i%2==0:
        print(i*i) #squares of first 10 even numbers


for i in range(20,0,-2):
    print(i)       


for i in range(10,0,-1):
    print(i)    #numbers in reverse 


for i in range(1,20):
    if i%2!=0:
        print(i)  #odd numbers from 1 to 20


word = "python"
for i in word:
    print(i)  #for loop with a string


word = "python"
for i in word :
    if i in "aeiou" :
        print(i)  #printing vowels from the word


word = input("Enter your word: ")
for i in word :
    if i in "aeiou" or i in  "AEIOU":
        print(i)        


word = input("Enter your word: ")
for i in word :
    if i.lower() in "aeiou":
        print(i)  #optimised version


word = input("Enter your word: ")
count = 0
for i in word :
    if i.lower() in "aeiou":
        count = count + 1
print(count)  #printing the count of vowels


word = "python"
for index , char in enumerate(word):
    print(index,char) #enumerate function to get index and character


for i in range (1,6):
    for j in range(1 , i+1):
        print(j,end=" ")
    print()    #pattern printing
    

for i in range (6,0,-1):
    for j in range(1 , i+1):
        print(j,end=" ")
    print()
