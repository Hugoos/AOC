import math
import ast 
from AOCTools import *
from tqdm import tqdm
import copy
import numpy as np
from time import sleep
from collections import deque
#fileName = "input/input14.txt" #no inputfile

startingNumbers = [0,13,1,16,6,17]
#startingNumbers = [3,1,2]
spoken = {}
firstTime = False
for i, num in enumerate(startingNumbers):
    if not num in spoken:
        nextSpoken = 0
    else:
        nextSpoken = i - spoken[num]
    spoken[num] = i+1
    lastSpoken = num
   
i = len(startingNumbers) + 1
end = 30000000
#end = 2020
print(spoken)
pbar = tqdm(total=end)
print("nextSpoken is: " + str(nextSpoken))
while True:
    #pbar.update(1)
    if not nextSpoken in spoken:
        currentSpoken = nextSpoken
        spoken[nextSpoken] = i
        nextSpoken = 0
    else:
        currentSpoken = nextSpoken
        nextSpoken = i - spoken[currentSpoken]
        spoken[currentSpoken] = i
        
         
    if i == end:
        print(currentSpoken)
        break
    #print(i, spoken)
    #print("nextSpoken is: " + str(nextSpoken))
    i += 1
    
    
