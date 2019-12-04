import math
import numpy as np
import re
import operator

name2 = "input/input6.txt" #pentest
f=open(name2)
originList = []
originDict = {}
candidates = {}
x_list = []
y_list = []
A = f.readlines()

def hDistance(co1, co2):
    return(abs(co1[0] - co2[0]) + abs(co1[1] - co2[1]))

print(hDistance((1,1),(2,2)))

for q in A:
    x, y = q.split(",")
    x = int(x)
    y = int(y)
    x_list.append(x)
    y_list.append(y)
    originList.append((x,y))
    xmin = min(x_list)
    xmax = max(x_list)
    ymin = min(y_list)
    ymax = max(y_list)
    xmininf = xmin - 1
    xmaxinf = xmax + 1
    ymininf = ymin - 1
    ymaxinf = ymax + 1
print(xmin,xmax,ymin,ymax)

for x in originList:
    originDict[x] = 0

for x in range(xmin,xmax+1):
    for y in range(ymin,ymax+1):
        hDistanceList = []
        for xy in originList:
            hDistanceList.append(hDistance((x,y),xy))
        m = min(hDistanceList)
        minList = [i for i, j in enumerate(hDistanceList) if j == m]
        if len(minList) == 1:
            originDict[originList[minList[0]]] += 1
            
removeSet = set()
for x in range(xmininf,xmaxinf+1):
    for y in range(ymininf,ymaxinf+1):
        if not x == xmininf or x == xmaxinf or y == ymininf or y == ymaxinf:
            continue
        hDistanceList = []
        for xy in originList:
            hDistanceList.append(hDistance((x,y),xy))
        m = min(hDistanceList)
        minList = [i for i, j in enumerate(hDistanceList) if j == m]
        if len(minList) == 1:
            removeSet.add(originList[minList[0]])

for key in removeSet:
    del originDict[key]

print(removeSet)
print(originDict)
print(max(originDict.values()))
print(max(originDict, key=originDict.get))
            
            
