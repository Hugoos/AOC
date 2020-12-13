import math
import ast 
from AOCTools import *
import copy
import numpy as np
fileName = "input/input12.txt" #pentest

lines= read_strings(fileName)
facing = 0
directionDict = {270: np.array([0,1]), 0: np.array([1,0]), 90: np.array([0,-1]), 180: np.array([-1,0]),"N": np.array([0,1]), "E": np.array([1,0]), "S": np.array([0,-1]), "W": np.array([-1,0]), "L": -1, "R": 1}
location = (0,0)
waypointLocation = (10,1)

for line in lines:
    instruction = line[0]
    value = int(line[1:])
    if instruction == "L" or instruction == "R":
        if instruction == "L":
            value = 360 - value
        waypointLocation = rotateXY(waypointLocation,value)

    elif instruction == "F":
        location = (location[0] + waypointLocation[0] * value,location[1] + waypointLocation[1] * value)
    else:
        waypointLocation = (waypointLocation[0] + directionDict[instruction][0] * value,waypointLocation[1] + directionDict[instruction][1] * value)

print(int(round(abs(location[0]) + abs(location[1]))))
      
  
    
    

