#Dhilan Patel
#Create a list of at least 5 elements (or ask the user to give the Values)
#Create a menu similar to what we did for the Strings MEthods
#in each selection you will allow the user to:
#1 insert elements either appending or inserting
#2 delete an element either by value or by index
#3  find if something in the list
#4  Find the index where an element is in the list
#5 reverse the order of the array
#Global Var
myNumbers=[1, 2, 3, 4, 5, 6, 7, 8, 9]
myList=["Alpha", "Beta", "Gamma", "Delta"]
string= "Hello World"
rstring="dlroW olleH"
x=1
rstrg= False
cnvrtTxt= 1
convert= False
menu2= True
cont= False

#Menu Text
l1= "**************************"
l2= "*       My game          *"
l3= "*                        *"
l4= "*    1 - List            *"
l5= "*    2 - Convert String  *"
l6= "*    3 - Scores          *"
l7= "*    4 - Exit            *"
ls1="*        Scores          *"
ls2="*    1 - ???- 999        *"
ls3="*    2 - ???- 876        *"
ls4="*    3 - ???- 745        *"
lc1="*   Text Conversions     *"
lc2="*    1 - Lowercase       *"
lc3="*    2 - Uppercase       *"
lc4="*    3 - Title case      *"
lc5="*    4 - Reverse:True    *"
lc6="*    4 - Reverse:False   *"
lc7="*    5 - Exit            *"
ll1="*     List Editor        *"
ll2="*    1 - Show List       *"
ll3="*    2 - Search List     *"
ll4="*    3 - Add Item        *"
ll7="*    4 - Remove Item     *"
ll5="*    5 - Reverse List    *"
ll6="*    6 - Exit            *"
#Functions
#Main Menu
def menu():
    print(l1)
    print(l2)
    print(l3)
    print(l4)
    print(l5)
    print(l6)
    print(l7)
    print(l1)
    print("Input a number from 1-4 to chose your selection:")
    x = input()
    return(x)
#Score Menu
def scoreM():
    print(l1)
    print(ls1)
    print(l3)
    print(ls2)
    print(ls3)
    print(ls4)
    print(l3) 
    print(l1)
def txtM():
    print(l1)
    print(lc1)
    print(l3)
    print(lc2)
    print(lc3)
    print(lc4)
    if (rstrg==False):
        print(lc6)
    if (rstrg==True):
        print(lc5)
    print(lc7)
    print(l1)
    print("Input a number from 1-5 to chose your selection:")
    cnvrtTxt = input()
    return(cnvrtTxt)
def listM():
    print(l1)
    print(ll1)
    print(l3)
    print(ll2)
    print(ll3)
    print(ll4)
    print(ll7)
    print(ll5) 
    print(ll6)
    print(l1)
    print("Input a number from 1-5 to chose your selection:")
    listTxt = input()
    return(listTxt)
#Confirmation
#def confrm():
#    print("Enter any key contine:")
#    Cnfrm= input()
#    while not Cnfrm:
#        Cnfrm= input()
def pause():
    print("Press enter to continue:")
    input()
#def stay():
#    print("Do you want to convert another string?")
#    print("Y/N")
#    anwser=input()
#    if (anwser=="Y"):
#        cont= True
#    if (anwser=="N"):
#        menu2=False
#        return(menu2, cont)
#Game    
while x !=4:
    x=menu()
    y = int(x)
    if(y==1): #Option 1 Play Game
        print("List Chosen")
        listMenu=True
        while (listMenu==True):
            listTxt= listM()
            optionl= int(listTxt)
            if (optionl==1): #Show List
                print("Show list")
                print(myList)
                pause()
            if (optionl==2): #Search List
                print("Search List")
                print("Enter what word you want to search for:")
                answer=input()
                if answer in myList:
                    print(answer, "is in the List.")
                    print(answer, "is number", myList.index(answer), "on the list.")
                else:
                    print(answer, "is in the List.")
                pause()
            if (optionl==3): #Add List
                    print("Add Item")
                    print("Name the item you would like to add:")
                    myList.append(input())
            if (optionl==4): #Remove List
                    print("Remove Item")
                    print("Name the item you would like to remove:")
                    myList.remove(input())
            if (optionl==5): #Reverse List
                print("Reverse List")
                myList.reverse()
            if (optionl==6): #Exit
                listMenu=False
    if(y==2): #Option 2 Convert Stuff
        print("Convert String")
        convert=True
        while (convert==True):
            cnvrtTxt= txtM()
            option= int(cnvrtTxt)
            if (option==1): #Lower
                menu1=True
                while (menu1==True):
                    print("Input a sentance:")
                    string= input()
                    print("")
                    rstring= string[::-1]
                    if (rstrg==True):
                        print(rstring.lower())
                    if (rstrg==False):
                        print(string.lower())
                    print("Do you want to convert another string?")
                    print("Y/N")
                    anwser=input()
                    if (anwser=="Y"):
                        continue
                    if (anwser=="N"):
                        menu1=False
            if (option==2): #Upper
                menu1=True
                while (menu1==True):
                    print("Input a sentance:")
                    string= input()
                    print("")
                    rstring= string[::-1]
                    if (rstrg==True):
                        print(rstring.upper())
                    if (rstrg==False):
                        print(string.upper())
                    print("Do you want to convert another string?")
                    print("Y/N")
                    anwser=input()
                    if (anwser=="Y"):
                        continue
                    if (anwser=="N"):
                        menu1=False
            if (option==3): #Title
                menu1=True
                while (menu1==True):
                    print("Input a sentance:")
                    string= input()
                    print("")
                    rstring= string[::-1]
                    if (rstrg==True):
                        print(rstring.title())
                    if (rstrg==False):
                        print(string.title())
                    print("Do you want to convert another string?")
                    print("Y/N")
                    anwser=input()
                    if (anwser=="Y"):
                        continue
                    if (anwser=="N"):
                        menu1=False
            if (option==4): #Reverse true/false
                if (rstrg==True):
                    rstrg=False
                    continue
                if (rstrg==False):
                    rstrg=True
                    continue
            if (option==5): #Exit
                convert=False
    if(y==3): #Option 3 Scores
        print("Scores Chosen")
        scoreM()
        pause()
    if(y==4): #Option 4 Exit
        print("Exit Game")
        print("Are you sure?")
        print("Y/N")
        anwser=input()
        if (anwser=="Y"):
            break
        if (anwser=="N"):
            continue