import math
import ast 
from AOCTools import *
import copy
import numpy as np
fileName = "input/input13.txt" #pentest

lines= read_strings(fileName, deliminator=",")
earliestTimestamp = int(lines[0][0])
busIds = lines[1]
#earliestTimestamp = 939
#busIds = [7,13,"x","x",59,"x",31,19]

def findEarliestBus():      
    i = 0  
    while True:
        for busId in [x for x in busIds if not x == "x"]:
            if (earliestTimestamp + i) % int(busId) == 0:
                return(int(busId) * i)
        i += 1
print(findEarliestBus())
    
    

