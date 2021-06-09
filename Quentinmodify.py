#Dhilan Patel
#Quentin Modify
#6/8/21
l1="**************************"
l2="*       My game          *"
l3="*                        *"
l4="*    1 - Capitalize      *"
l5="*    2 - Level2          *"
l6="*    3 - Scores          *"
l7="*    4 - Exit Game       *"
l8="**************************"
x=1  #global variable
def menu():
    print(l1)
    print(l2)
    print(l3)
    print(l4)
    print(l5)
    print(l6)
    print(l7)
    print(l8)
    print("please enter your selection from 1 to 4")
    inputNumber = input()
    x = int(inputNumber)
    return x
def score():
    print(l1)
    print("*        Scores          *")
    print(l3)
    print("*    1 - ???- 999        *")
    print("*    2 - ???- 876        *")
    print("*    3 - ???- 745        *")
    print(l3)
    print(l8)
def pause():
    print("Press enter to conginue")
    input()
while x !=4:  
    x=menu()
    if(x==1):        #if statement are selection or branching
        print("Level 1 Chosen")
        print("Please ener a phrase in lower case")
        answer=input() #input is a function
        print(answer.capitalize()) #is a method of strings and you have to refered with a dot 
        answer=answer.capitalize() #update your variable to the new change if I dont need orginal value 
        print(answer)
        pause()
    if(x==2):
        print("Level 2 Chosen")
 
    if(x==3):
        score()
 
print("Goodbye, Thank you for playing")