import math
name2 = "input/input3.txt" #pentest
f=open(name2)
lines=f.readlines()

coordsDict = {}
DirectionX = {"^": 0, "<": -1, ">": 1, "v": 0}
DirectionY = {"^": 1, "<": 0, ">": 0, "v": -1} 

def addCoord(x,y):
    if (x,y) not in coordsDict:
        coordsDict[(x,y)] = 1
    else:
        coordsDict[(x,y)] = coordsDict[(x,y)] + 1

class Santa:
    def __init__(self, x, y):
        self.x = 0
        self.y = 0
        self.deliverPresent()
        
    def move(self, dx,dy):
        self.x += dx
        self.y += dy
        self.deliverPresent()

    def deliverPresent(self):
        addCoord(self.x,self.y)
    
santa = Santa(0,0)
robo_santa = Santa(0,0)
santaList = [santa,robo_santa]
santaTurn = 0
    
for l in lines:
    for l2 in l:
        santaList[santaTurn].move(DirectionX[l2],DirectionY[l2])
        santaTurn = (santaTurn + 1) % 2

print(len(coordsDict))
        
