import math
from AOCTools import *
import numpy as np 
fileName = "input/input1.txt" #pentest

lines= read_strings(fileName, commas = True)
#lines = ["R8", "R4", "R4", "R8"]
directionDict = {0: np.array([0,1]), 1: np.array([1,0]), 2: np.array([0,-1]), 3: np.array([-1,0])}
DxDy = {"R": 1, "L": -1}
direction = 0
location = np.array([0,0])
locationList = [(0,0)]
for x in lines:
    direction = (direction + DxDy[x[0]]) % 4
    for x in range(int(x[1:])):
        location += directionDict[direction]
        if (location[0],location[1]) in locationList:
            #print(location)
            print(abs(location[0]) + abs(location[1]))
            break
        else:
            locationList.append((location[0],location[1]))

#print(locationList)
#print(abs(location[0]) + abs(location[1]))
