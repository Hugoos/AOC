import math
from Machine import Machine
from collections import namedtuple
import csv
import numpy as np
from PIL import Image
import random
import Astar
name2 = "input/input18.txt"

Coordinate = namedtuple("Coordinate", 'x y')
DX = {'L': -1, 'R': 1, 'U': 0, 'D': 0}
DY = {'L': 0, 'R': 0, 'U': -1, 'D': 1}
movementCommand = {'L': 3, 'R': 4, 'U': 1, 'D': 2}
directionList = ["U","R","D","L"]
coordDict = {}

f=open(name2)
lines=f.readlines()

lines = [line.replace("\n","") for line in lines]
print(lines)
#lines = ["########################",
#"#@..............ac.GI.b#",
#"###d#e#f################",
#"###A#B#C################",
#"###g#h#i################",
#"########################"]
keyDict = {}
doorDict = {}
print(lines)
maze = np.ones((len(lines),len(lines[0])))
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == "." or char == "@":
            if char == "@":
                location = (y,x)
            maze[y][x] = 0
        elif char.islower():
            maze[y][x] = 0
            keyDict[char] = (y,x)
        elif char.isupper():
            doorDict[char] = (y,x)

print(maze)
print(doorDict)
print(keyDict)
print(location)
        
distanceList = []
itt = 0

def goKey(maze, location, distance, keyDict, doorDict):
    global itt
    #print(keyDict)
    lenDict = {}
    routeSet = set()
    if not keyDict:
        distanceList.append(distance)
        itt = (itt + 1) % 100
        if itt == 0: print(min(distanceList))
        return 1
    for key in keyDict:
        route = Astar.astar(maze, location, keyDict[key])
        lenDict[key] = len(route)
        routeSet.update(route[1:])
    keyDictReachable = [value for value in set(keyDict.values()) - routeSet]
    keyDictReachable = [key for key in keyDict.keys() if keyDict[key] in keyDictReachable]
    #print(keyDictReachable)
    for key in keyDictReachable:
        #print(location)
        #print(keyDict[key])
        #print(Astar.astar(maze, location, keyDict[key]))
        distanceToKey = lenDict[key]
        if distanceToKey > 0:
            newMaze = np.array(maze, copy=True)
            if key.upper() in doorDict:
                unlockedDoor = doorDict[key.upper()]
                newMaze[unlockedDoor[0]][unlockedDoor[1]] = 0
            #print(newMaze)
            newDistance = distance + distanceToKey
            #print(newDistance)
            newLocation = keyDict[key]
            newKeyDict = keyDict.copy()
            #newDoorDict = doorDict.copy()
            del newKeyDict[key]
            #if key.upper() in doorDict:
            #    del newDoorDict[key.upper()]
            goKey(newMaze, newLocation, newDistance, newKeyDict, doorDict)
        
goKey(maze, location, 0, keyDict, doorDict)
print(min(distanceList))


    

