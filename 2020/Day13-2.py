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
#busIds = [1789,37,47,1889] #1202161486

busIds = [(i,x) for i,x in enumerate(busIds) if not x == "x"]
print(busIds)
def findMultiplier(start):
    skip = 1
    t = start
    lcmList = []
    for i,x in busIds:
        while True:
            if (t+i) % int(x) == 0:
                lcmList.append(int(x))
                skip = np.prod(lcmList,dtype=np.int64)
                break
            t += skip
    return t
            
        
            
    

print(findMultiplier(1))
    
