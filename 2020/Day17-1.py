import math
import ast 
from AOCTools import *
import copy
import numpy as np
import itertools as it
fileName = "input/input17.txt"
lines = read_strings(fileName)


perm = list(it.product((-1,0,1), repeat=3))
perm.remove((0,0,0))
activeSet = set([])

for y,line in enumerate(lines):
    for x,char in enumerate(line):
        if char == "#":
            activeSet.add((x,y,0))
print(activeSet)
def getNeighbours(x,y,z):
    neighbours = set([])
    for x2,y2,z2 in perm:
        neighbours.add((x+x2,y+y2,z+z2))
    return neighbours

def getActiveNeighbours(x,y,z):
    count = 0
    for x2,y2,z2 in perm:
        if ((x+x2,y+y2,z+z2) in activeSet):
            count += 1
    return count
i = 0
while i < 6:
    activeSetNew = set([])
    inactiveNeighboursSet = set([])
    for x,y,z in activeSet:
        inactiveNeighboursSet.update(getNeighbours(x,y,z))

    inactiveNeighboursSet = inactiveNeighboursSet - activeSet

    for x,y,z in activeSet:
        if 2 <= getActiveNeighbours(x,y,z) <= 3:
            activeSetNew.add((x,y,z))
    for x,y,z in inactiveNeighboursSet:
        if getActiveNeighbours(x,y,z) == 3:
            activeSetNew.add((x,y,z))
    activeSet = activeSetNew
    i += 1
print(len(activeSet))
    
    
