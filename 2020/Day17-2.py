import math
import ast 
from AOCTools import *
import copy
import numpy as np
import itertools as it
fileName = "input/input17.txt"
lines = read_strings(fileName)


perm = list(it.product((-1,0,1), repeat=4))
perm.remove((0,0,0,0))
activeSet = set([])
print(len(perm))
for y,line in enumerate(lines):
    for x,char in enumerate(line):
        if char == "#":
            activeSet.add((x,y,0,0))
print(activeSet)
def getNeighbours(x,y,z,w):
    neighbours = set([])
    for x2,y2,z2,w2 in perm:
        neighbours.add((x+x2,y+y2,z+z2,w+w2))
    return neighbours

def getActiveNeighbours(x,y,z,w):
    count = 0
    for x2,y2,z2,w2 in perm:
        if ((x+x2,y+y2,z+z2,w+w2) in activeSet):
            count += 1
    return count
i = 0
while i < 6:
    activeSetNew = set([])
    inactiveNeighboursSet = set([])
    for x,y,z,w in activeSet:
        inactiveNeighboursSet.update(getNeighbours(x,y,z,w))

    inactiveNeighboursSet = inactiveNeighboursSet - activeSet

    for x,y,z,w in activeSet:
        if 2 <= getActiveNeighbours(x,y,z,w) <= 3:
            activeSetNew.add((x,y,z,w))
    for x,y,z,w in inactiveNeighboursSet:
        if getActiveNeighbours(x,y,z,w) == 3:
            activeSetNew.add((x,y,z,w))
    activeSet = activeSetNew
    i += 1
print(len(activeSet))
    
    
