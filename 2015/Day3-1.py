import math
name2 = "input/input3.txt" #pentest
f=open(name2)
lines=f.readlines()

coordsDict = {}

def addCoord(x,y):
    if (x,y) not in coordsDict:
        coordsDict[(x,y)] = 1
    else:
        coordsDict[(x,y)] = coordsDict[(x,y)] + 1
    
DirectionX = {"^": 0, "<": -1, ">": 1, "v": 0}
DirectionY = {"^": 1, "<": 0, ">": 0, "v": -1} 
x = 0
y = 0
addCoord(x,y)
for l in lines:
    for l2 in l:
        x += DirectionX[l2]
        y += DirectionY[l2]
        addCoord(x,y)

print(len(coordsDict))
        
