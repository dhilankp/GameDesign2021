#We are going to learn how to create files
#Dhilan Patel
import os
import sys
import time 

#using time to pause your games

print("Hello")
time.sleep(2)
print("there")
def readFile():
    file= input("What is the name of the file?")
    if os.path.exists(file): #It is to make sure the file exists 
        PEN=open(file, 'r')
        print(PEN.read())
    else:
        print("The file does not exist! Thank you")
fileName="DhilanGame.txt"
if os.path.exists(fileName):
    print("Sorry that file exists")
else:
    FILE=open(fileName, 'w')
    FILE.write("******** THIS IS DHILAN'S FILE*******")
    FILE.close()
    time.sleep(1)
    FILE=open(fileName, 'r')
    print(FILE.read())
    FILE.close()
File=open("DhilanGame.txt", 'a')
newline= "\n What ever"
File.write(newline)
File.close()