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

state = np.zeros((20,42))
machine = Machine(data=data.copy())

while True:
    x = next(machine.run())
    if x == 1:
        break
    x = x[0]
    y = next(machine.run())[0]
    tileId = next(machine.run())[0]
    #print(x, y, tileId)
    state[y][x] = tileId

remainingBlocks = np.count_nonzero(state == 2)
print(remainingBlocks)


im = Image.fromarray(state.astype('uint8')*255)
#im = Image.fromarray(image)
#if im.mode != 'RGB':
#    im = im.convert('RGB')
im.save("gamefield2.png")

    

