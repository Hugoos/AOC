import math
from Machine import Machine
from collections import namedtuple
import csv
import numpy as np
from PIL import Image
import random
import Astar
name2 = "input/input15.txt"

Coordinate = namedtuple("Coordinate", 'x y')
DX = {'L': -1, 'R': 1, 'U': 0, 'D': 0}
DY = {'L': 0, 'R': 0, 'U': -1, 'D': 1}
movementCommand = {'L': 3, 'R': 4, 'U': 1, 'D': 2}
directionList = ["U","R","D","L"]
coordDict = {}

with open(name2, 'r') as f:
    reader = csv.reader(f)
    data = list(reader)

data = data[0]
data = list(map(int, data))
data_orig = data.copy()

state = np.zeros((21,42))
machine = Machine(data=data.copy())
coordDict = {}
#machine.setMemory(0,2)
#frame = 1 
noChanges = 0
x = 0
y = 0
coordDict[(x,y)] = 1
cannisterFound = False
while noChanges < 10000 or not cannisterFound:
    direction = random.choice(directionList)
    machine.setInput([movementCommand[direction]])
    machineCode = next(machine.run())[0]
    noChanges += 1
    if machineCode > 0:
        x += DX[direction]
        y += DY[direction]
        if not (x,y) in coordDict:
            print("New coord")
            coordDict[(x,y)] = machineCode
            noChanges = 0
            if machineCode == 2:
                print("Found canister")
                cannisterFound = True

print(coordDict)
minx = min([key[0] for key in coordDict.keys()])
maxx = max([key[0] for key in coordDict.keys()])
miny = min([key[1] for key in coordDict.keys()])
maxy = max([key[1] for key in coordDict.keys()])
print(minx, maxx)
print(miny, maxy)
origin = (0,0)
canister = [x for x in coordDict.keys() if coordDict[x] == 2][0]
print(origin)
print(canister)
offsetx = abs(minx)
offsety = abs(miny)
coordDictOffset = [(key[0]+offsetx,key[1]+offsety) for key in coordDict.keys()]
origin = (origin[1]+offsety,origin[0]+offsetx)
canister = (canister[1]+offsety,canister[0]+offsetx)
print(origin)
print(canister)
print(maxx + offsetx+1, maxy + offsety+1)
maze = np.ones((maxy + offsety+1, maxx + offsetx+1))

for coord in coordDictOffset:
    maze[coord[1]][coord[0]] = 0
maze = maze.astype(int)
#im = Image.fromarray(maze.astype('uint8')*100)
#im.save("maze" + ".png")
print(origin)
print(canister)
print(maze[origin[1]][origin[0]])
print(maze[canister[1]][canister[0]])
distanceList = [len(Astar.astar(maze, canister, location)) for location in coordDictOffset]
print(max(distanceList))
#route = route + [origin]
#route = route[::-1]
#print(route)
#print(len(route))
#print(path)


    

