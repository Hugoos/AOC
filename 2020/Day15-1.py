import math
import ast 
from AOCTools import *
import copy
import numpy as np
#fileName = "input/input14.txt" #no inputfile

startingNumbers = [0,13,1,16,6,17]
#startingNumbers = [3,1,2]
spoken = {}
spoken[0] = []
for i, num in enumerate(startingNumbers):
    spoken[num] = []
    spoken[num].append(i+1)
    lastSpoken = num
   
i = len(startingNumbers) + 1

print(spoken)
while True:
    if len(spoken[lastSpoken]) == 1: #The word of the previous round was spoken for the first time
        spoken[0].append(i)
        lastSpoken = 0
    else: #The word was spoken before
        #print(spoken[lastSpoken][-2:])
        lastTwo = spoken[lastSpoken][-2:]
        #print(lastTwo)
        lastSpoken = lastTwo[1]-lastTwo[0]
        if not lastSpoken in spoken:
            spoken[lastSpoken] = []
        spoken[lastSpoken].append(i)
    if i == 2020:
        print(lastSpoken)
        break
    #print(i, spoken)
    i += 1
    
