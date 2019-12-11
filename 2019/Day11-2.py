import math
from Machine import Machine
from collections import namedtuple
import csv
import numpy as np
from PIL import Image
name2 = "input/input11.txt" #pentest

Coordinate = namedtuple("Coordinate", 'x y')
DX = {'L': -1, 'R': 1, 'U': 0, 'D': 0}
DY = {'L': 0, 'R': 0, 'U': -1, 'D': 1}
directionList = ["U","R","D","L"]
coordDict = {}

with open(name2, 'r') as f:
    reader = csv.reader(f)
    data = list(reader)

data = data[0]
data = list(map(int, data))
data_orig = data.copy()

machine = Machine(data=data.copy())
direction = "U"
position = Coordinate(0,0)
ready = False
coordDict[position] = 1
while True: 
    if position not in coordDict:
        coordDict[position] = 0
    mInput = [coordDict[position]]
    #print("mInput: " + str(mInput))
    color = next(machine.run(mInput))
    #print("color1: " + str(color))
    if color == 1:
        break
    turn = next(machine.run())
    #print("turn2: " + str(turn))
    coordDict[position] = color[0]
    
    index = directionList.index(direction)
    if turn[0]: #right
        index = (index + 1) % 4
    else: #left
        index = (index - 1) % 4
    direction = directionList[index]
    position = Coordinate(position.x + DX[direction], position.y + DY[direction])
#print(coordDict)
minx = min([coord.x for coord in coordDict])
maxx = max([coord.x for coord in coordDict])
miny = min([coord.y for coord in coordDict])
maxy = max([coord.y for coord in coordDict])

image = np.zeros((maxy+1,maxx+1))
for coord in coordDict:
    image[coord.y][coord.x] = coordDict[coord]

im = Image.fromarray(image.astype('uint8')*255)
#im = Image.fromarray(image)
#if im.mode != 'RGB':
#    im = im.convert('RGB')
im.save("image11.png")
