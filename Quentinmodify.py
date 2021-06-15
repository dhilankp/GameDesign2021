#Dhilan Patel
#Quentin Modify
#6/8/21
l1="********************************"
l2="*       My game                *"
l3="*                              *"
l4="*    1 - Capitalize            *"
l5="*    2 - Uppercase             *"
l6="*    3 - Lowercase             *"
l7="*    4 - Find index of char    *"
l8="*    5 - Split                 *"
l9="*    6 - Translate             *"
l10="*    7 - Exit                  *"
l11="********************************"
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
    print(l9)
    print(l10)
    print(l11)
    print("please enter your selection from 1 to 7")
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
    print("Do you want to play again?")
    answer1= input()
    answer1=answer1.upper()
    if "Y" in answer1:
        return True
    else:
        return False

while x !=7:  
    x=menu()
    if(x==1):        #if statement are selection or branching
        convert=True
        while convert:
            print("Captialize Chosen")
            print("Please ener a phrase in lower case")
            answer=input() #input is a function
            answer=answer.capitalize() #update your variable to the new change if I dont need orginal value 
            print(answer)
            convert=pause()




        # let the user stay in the level and reuse it many times until they want to get back to main menu
    if(x==2):
        convert=True
        while convert:
            print("Uppercase Chosen")
            print("Please ener a phrase in lower case")
            answer=input() #input is a function
            answer=answer.upper() #update your variable to the new change if I dont need orginal value 
            print(answer)
            convert=pause()
            
    if(x==3):
        convert=True
        while convert:
            print("Lowercase Chosen")
            print("Please ener a phrase in upper case")
            answer=input() #input is a function
            answer=answer.lower() #update your variable to the new change if I dont need orginal value 
            print(answer)
            convert=pause()
    if(x==7):
        print("Goodbye, Thank you for playing!")
  