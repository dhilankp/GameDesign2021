#Dhilan Patel
#Create a list of at least 5 elements (or ask the user to give the Values)
#Create a menu similar to what we did for the Strings MEthods
#in each selection you will allow the user to:
#1 insert elements either appending or inserting
#2 delete an element either by value or by index
#3  find if something in the list
#4  Find the index where an element is in the list
#5 reverse the order of the array
l1= "**************************"
l2= "* My game                *"
l3= "* 1 - choose list        *"
l4= "* 2 - Delete element     *"
l5= "* 3 - insert element     *"
l6= "* 4 - find index         *"
l7= "* 5 - reverse order      *"
l9= "* 6 - find on list       *"      
l10="* 7 - exit to menu       *"
l8= "**************************"
x=1
def menu():
    print(l1)
    print(l2)
    print(l3)
    print(l4)
    print(l5)
    print(l6)
    print(l7)
    print(l9)
    print(l10)
    print(l8)
    print ("please enter number selection 1-5")
    inputNumber = input()
    x = int(inputNumber)
    return x 
while x !=7:
    x=menu()
    while (x==1):
        convert=True
        while convert:
            print ("Please choose list of five objects")
            mylist=input()
            x=7
            print("To replay level press 1")
            print("To go back to the main menu press 7")
            x=int(input())
    mylist=input
    while (x==2):
        convert=True
        while convert:
            print (mylist)
            print ("what element do you want to take out?")
            inputel=input()
            mylist.remove(inputel)
            x=7
            print("To replay level press 2")
            print("To go back to the main menu press 7")
            x=int(input())
    while (x==3):
        convert=True
        while convert:
            print (mylist)
            print ('After what item do you want to put your new item, and what is it (ex: 0, kiwi)')
            inputval=input()
            mylist.insert(inputval)
            #if inputval-1 ==5 (mylist.append(inputval))  how do i get it to append depending on where the user puts the value
            x=7
            print("To replay level press 2")
            print("To go back to the main menu press 7")
            x=int(input())
 