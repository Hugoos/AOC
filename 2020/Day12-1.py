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
#lines = ["F10",
#"N3",
#"F7",
#"R90",
#"F11"]
for line in lines:
    instruction = line[0]
    value = int(line[1:])
    if instruction == "L" or instruction == "R":
        facing = (facing + directionDict[instruction] * value) % 360

    elif instruction == "F":
        location = (location[0] + directionDict[facing][0] * value,location[1] + directionDict[facing][1] * value)
    else:
        location = (location[0] + directionDict[instruction][0] * value,location[1] + directionDict[instruction][1] * value)

print(abs(location[0]) + abs(location[1]))
      
  
    
    

