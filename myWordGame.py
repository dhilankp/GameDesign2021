#Dhilan Patel
# 06/11/2021
#Word Game
# we are creating a list of words 
# randomly select a word from the list for the user to guess 
# give the user some turns
# show the word to the user with the characters guessed 
# play the game as long as the user has turns or has guessed the word 
l1="********************************"
l2="*       Word Game              *"
l3="*                              *"
l4="*    1 - Play Game             *"
l5="*    2 - Print Top Scores      *"
l6="*    3 - Exit                  *"
l7="********************************"
x=1  #global variable
def menu():
    print(l1)
    print(l2)
    print(l3)
    print(l4)
    print(l5)
    print(l6)
    print(l7)
    print("please enter your selection from 1 to 3")
    inputNumber = input()
    x= int(inputNumber)
    return x
name=input("What is your name? ")
print("Hi", name, "here is the menu!")
score=0
while x !=3:  
    x=menu()
    if(x==1): 
        import random
        gameWords=['broncos','cheifs','raiders','chargers','seahawks','cardinals', 'rams', '49ers']
        answer=input("Do you want to guess a word? ")
        answer=answer.upper()
        def updateWord(word):
            for char in word:
                if char in guesses:
                    print(char, end=' ')
                else:
                    print('_', end=' ')
        while 'Y'in answer: 
            print ("Good luck", name, "!")
            word=random.choice(gameWords)
            counter=len(word)                                                                     
            print("There are",counter, "letters in the word")
            turns=10 #should we consider controlling this number when he/she misses
            guesses= ''
            updateWord(word)
            answer='changed'
        while turns>0 and counter>0:
            
            newGuess=input("\n\n Give me a letter ")
            if newGuess not in word:
                turns-=1 #turns=turns -1
                print ("Wrong! You have" , turns, "guesses left")
            else:
                rept=word.count(newGuess)
                counter-=rept
                print ("Nice guess!")
            guesses += newGuess
            updateWord(word)
            
            if(counter ==0):
                print("You guess correctly!")
                score=score+1
                word=random.choice(gameWords)
                counter=len(word)                                                                     
                print("There are",counter, "letters in the word")
                guesses= ''
                updateWord(word)
        while counter !=0:
            print("oops! you ran out of guesses! Your final score was",score,)        
            break
    x=input("To play again push 1")
        

if(x==3):
    print (name, "Thank you for playing!")