#Dhilan Patel
# 06/11/2021
#Word Game
# we are creating a list of words 
# randomly select a word from the list for the user to guess 
# give the user some turns
# show the word to the user with the characters guessed 
# play the game as long as the user has turns or has guessed the word 

import random
gameWords=['Broncos','Cheifs','Raiders','Chargers','Seahawks','Cardinals', 'Rams', '49ers']
answer=input("Do you want to guess a word? ")
name=input("What is your name? ")
answer=answer.upper()
while 'Y'in answer: 
    print ("Good luck", name, "!")
    word=random.choice(gameWords)
    counter=len(word)
    print(counter)
    turns=10 #should we consider controlling this number when he/she misses
    guesses= ''
    while turns>0 and counter>0:
        for char in word:
            if char in guesses:
                print (char, end=" " )
            else:
                print('_', end= " ")
        newGuess=input("\n\n Give me a letter ")
        if newGuess not in word:
            turns-=1 #turns=turns -1
            print ("Wrong! You have" , turns, "guesses left")
        else:
            counter -=1
            print ("Nice guess!")
        guesses += newGuess
#more to come
 
    answer=input("Would you like to play again?") .upper()
print (name, "Thank you for playing!")