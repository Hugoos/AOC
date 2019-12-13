import math
from Machine import Machine
from collections import namedtuple
import csv
import numpy as np
from PIL import Image
name2 = "input/input13.txt"

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

state = np.zeros((21,42))
machine = Machine(data=data.copy())
machine.setMemory(0,2)
frame = 1 

def printFrame():
    while True:
        x = next(machine.run())
        if x == 1:
            break
        x = x[0]
        y = next(machine.run())[0]
        tileId = next(machine.run())[0]
        #print(x, y, tileId)
        if x == -1 and y == 0:
            score = tileId
            return score
        #print(x, y, tileId)
        state[y][x] = tileId
    return -1

def update(frame):
    while True:
        x = next(machine.run())
        if x == 1:
            break
        x = x[0]
        y = next(machine.run())[0]
        tileId = next(machine.run())[0]
        #print(x, y, tileId)
        if x == -1 and y == 0:
            score = tileId
            return score, frame
        #print(x, y, tileId)
        state[y][x] = tileId
        if tileId == 4:
            im = Image.fromarray(state.astype('uint8')*255)

            im.save("Day13Images/gamefield" + str(frame) + ".png")
            frame += 1
            ballLocation = np.where(state == 4)
            paddleLocation = np.where(state == 3)
            ballx = ballLocation[1][0]
            paddlex = paddleLocation[1][0]
            if ballx < paddlex:
                machine.setInput([-1])
            elif ballx > paddlex:
                machine.setInput([1])
            else:
                machine.setInput([0])
    return -1

score = printFrame()
ballLocation = np.where(state == 4)
paddleLocation = np.where(state == 3)
ballx = ballLocation[1][0]
paddlex = paddleLocation[1][0]
if ballx < paddlex:
    machine.setInput([-1])
elif ballx > paddlex:
    machine.setInput([1])
else:
    machine.setInput([0])
while True:
    score, frame = update(frame)
    remainingBlocks = np.count_nonzero(state == 2)
    if remainingBlocks == 0:
        break

im = Image.fromarray(state.astype('uint8')*255)
im.save("Day13Images/gamefield" + str(frame) + ".png")
    
#remainingBlocks = np.count_nonzero(state == 2)
print(score)



    

