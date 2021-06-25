#Dhilan Patel
#6/16/2021
#We are going to learn how to open files, read files 
#How to read files per line
#How to make a list from files
#How to manipulate the elements to find what we need
import os
import sys
import time
os.system('cls')

file='challenge.txt'
File= open(file, 'r')
content=File.read()
print(content)
File.close()
File=open(file,'r')
content_Lists=File.readlines()
print(content_Lists)
File.close()
for element in content_Lists:
    print("line  : ", element)
    elem_list=element.split()
    print(elem_list)
    time.sleep(1)

from hashlib import new
from os import write
import os
 
scoredat="challenge.txt"
 
def pause():
    print("Press enter to continue:")
    input()
 
print("Scores Chosen")
with open(scoredat,'r') as first_file:   #open score archive
    rows = first_file.readlines()
    sorted_rows = sorted(rows, key=lambda x: int(x.split()[2]), reverse=True)
    with open(scoredat,'w+') as second_file:
        for row in sorted_rows:
            second_file.write(row)
first_file.close()
second_file.close()
writenScores = open(scoredat, "r")
displayScores = writenScores.read()
print(displayScores)
writenScores.close()
pause()