import math
import ast 
from AOCTools import *
import copy
from operator import itemgetter 
import numpy as np
fileName = "input/input16.txt" 
#fileName = "input/input16Example2.txt" 
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
        print(key)
        nextPart = x[0].split(": ")[1]
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
errorTickets = []
for ticket in nearbyTickets:
    for val in ticket:
        valid = False
        for r in allRanges:
            if int(r[0]) <= int(val) <= int(r[1]):
                valid = True
        if not valid:
            errorTickets.append(ticket)
nearbyTicketsValid = []
for ticket in nearbyTickets:
    if not ticket in errorTickets:
        nearbyTicketsValid.append(ticket)

print(nearbyTicketsValid)
            
ticketsByColumn = []

for i in range(len(nearbyTicketsValid[0])):
    ticketsByColumn.append(list( map(itemgetter(i), nearbyTicketsValid )))
print(ticketsByColumn)
columnDict = {}
for i, vals in enumerate(ticketsByColumn):
    columnDict[i] = []
    #print("-------\n")
    for k,v in rangesDict.items():
        valid = True
        for val in vals:
            #print(val)
            #print(v)
            if not ((int(v[0][0]) <= int(val) <= int(v[0][1])) or (int(v[1][0]) <= int(val) <= int(v[1][1]))):
                #print("not valid")
                valid = False  
        if valid:
            columnDict[i].append(k)

print(columnDict)
i = 0
while i < 50:
    i += 1
    for k,v in columnDict.items():
        if len(v) == 1:
            for k2,v2 in columnDict.items():
                if (not k == k2) and (v[0] in v2):
                    newEntry = columnDict[k2]
                    newEntry.remove(v[0])
                    columnDict[k2] = newEntry
print(columnDict)
                
departureIndices = [5,8,10,13,16,18] #cba to do this programatically, will have to manually create this list for other input
solution = 1
for i in departureIndices:
    solution *= int(myTicket[i])
print(solution)
