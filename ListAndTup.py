#Dhilan Patel
#We are learning about List and Tuples
#Learn their functions and looping with List 

#How to import a module or library by importing 
import random

myFruit=["apples", "berries", "mangos", "banana"]
print(myFruit)
for fruit in myFruit:
    print (fruit)

for fruit in myFruit: #For the length of your array
    print(fruit, end=", ")
print()
counter=len(myFruit) #the length of you list is one more than tyour last index
#finding a random number to be the index to select randint()
indx= random.randint(0, counter-1)
print("your lucky fruit is ", myFruit[indx] )

#radnom method choice()
word=random.choice(myFruit)
print("Your random ruity is ", word)

for x in range(0,counter-1):
    print(myFruit[x], end=", ")

print(myFruit[counter-1]) #print the last element 

if "apples" in myFruit:
    print("yes you got apples")
    myFruit.remove("apples")
    print(myFruit)
myFruit.insert(0,"kiwi")
myFruit.insert(2,"papaya")
myFruit.append("beets")
print(myFruit)

fruity=("apple", "pears", "banana") #tuple
print("tuple", fruity)   #temp is a list
temp=list(fruity)
print("list", temp)
temp.insert(1, "kiwi")
fruity=tuple
print("tuple modified", fruity)
print("list modified", temp)
