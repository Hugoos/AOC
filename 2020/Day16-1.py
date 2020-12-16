import math
import ast 
from AOCTools import *
import copy
import numpy as np
fileName = "input/input16.txt" 
#fileName = "input/input16Example.txt" 
lines= read_strings(fileName, deliminator=",", vertDeliminator=" ")
#print(lines)
rangesDict = {}
nearbyTickets = []
i = 0
for x in lines[0]:
    if x[0] == "":
        i+= 1
        continue
    if i == 0: #load ranges
        key = x[0].split(": ")[0]
        nextPart = key = x[0].split(": ")[1]
        val1 = nextPart.split(" ")[0]
        val2 = nextPart.split(" ")[2]
        #print(key,val1,val2)
        rangesDict[key] = [(val1.split("-")[0],val1.split("-")[1]),(val2.split("-")[0],val2.split("-")[1])]
    if i == 1:
        myTicket = x
    if i == 2 and not x[0] == "nearby tickets:":
        nearbyTickets.append(x)
#print(rangesDict.values())
allRanges = [j for sub in rangesDict.values() for j in sub]
#print(allRanges)
errorVals = []
for ticket in nearbyTickets:
    for val in ticket:
        valid = False
        for r in allRanges:
            if int(r[0]) <= int(val) <= int(r[1]):
                valid = True
        if not valid:
            errorVals.append(int(val))
print(sum(errorVals))
            
                
