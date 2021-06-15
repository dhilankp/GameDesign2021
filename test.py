import time
import os
import sys
def printscores():
    file="wordgame.txt"
    Filer=open(file, 'r')
    print(Filer.read())
    Filer.close()

printscores()