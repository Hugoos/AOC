import math
from Machine import Machine
from collections import namedtuple
import csv
import numpy as np
from PIL import Image
import random
import Astar
name2 = "input/input17.txt"

Coordinate = namedtuple("Coordinate", 'x y')
DX = {'L': -1, 'R': 1, 'U': 0, 'D': 0}
DY = {'L': 0, 'R': 0, 'U': -1, 'D': 1}
movementCommand = {'L': 3, 'R': 4, 'U': 1, 'D': 2}
directionList = ["U","R","D","L"]
robotMap = []
robotMap.append([])

with open(name2, 'r') as f:
    reader = csv.reader(f)
    data = list(reader)

data = data[0]
data = list(map(int, data))
data_orig = data.copy()

state = np.zeros((21,42))
machine = Machine(data=data.copy())
machine.setMemory(0,2)

input_instructions = [",".join([str(x) for x in [ord('A'), ord(','), ord('B'), ord(','), ord('A'), ord(','), ord('C'), ord(','), ord('B'), ord(','), ord('C'), ord(','),
                      ord('B'), ord(','), ord('C'), ord(','), ord('A'), ord(','), ord('C'), ord('\n')]]),
                      ",".join([str(x) for x in [ord('L'), ord(','), ord('1'), ord('0'), ord(','), ord('R'), ord(','), ord('1'), ord('2'), ord(','), ord('R'), ord(','), ord('1'), ord('2'), ord('\n')]]),
                      ",".join([str(x) for x in [ord('R'), ord(','), ord('6'), ord(','), ord('R'), ord(','), ord('1'), ord('0'), ord(','), ord('L'), ord(','), ord('1'), ord('0'), ord('\n')]]),
                      ",".join([str(x) for x in [ord('R'), ord(','), ord('1'), ord('0'), ord(','), ord('L'), ord(','), ord('1'), ord('0'), ord(','), ord('L'), ord(','), ord('1'), ord('2'), ord('R'), ord(','), ord('6'), ord('\n')]]),
                      ",".join([str(x) for x in [ord('n'), ord('\n')]])]
inputList = []            
for line in input_instructions:
    for char in line.split(","):
        inputList.append(int(char))
machine.setInput(inputList)
index = 0
while True:
    outp = next(machine.run())
    if outp == 1:
        break
    if outp[0] == 10:
        robotMap.append([])
        index += 1
    else:
        robotMap[index].append(chr(outp[0]))
robotMap.pop()
robotMap.pop()
print(robotMap)
coordList = []
for y in range(len(robotMap)-2):
    y = y+1
    #print(y)
    for x in range(len(robotMap[y])-2):
        x = x+1
        #print(x)
        #try:
        if robotMap[y][x] == "#" and robotMap[y+1][x] == "#" and robotMap[y-1][x] == "#" and robotMap[y][x+1] == "#" and robotMap[y][x-1] == "#":
            coordList.append((x,y))
        #except:
        #    continue
summetje = 0
for coord in coordList:
    summetje += coord[0] * coord[1]
print(summetje)

for s in robotMap:
    print(*s)

pattern = ["L10","R12","R12","R6","R10","L10","L10","R12","R12","R10","L10","L12","R6","R6","R10","R12","R10","L10","L12","R6","R6","R10","L10","R10","L10","L12","R6","L10","R12","R12","R10","L10","L12","R6"]

def get_pattern(seq):
    seq2=seq
    outs={}
    l=0
    r=0
    c=None
    for end in range(len(seq2)+1):
        for start in range(end):
            word=chr(1).join(seq2[start:end])
            if not word in outs:
                outs[word]=1
            else:
                outs[word]+=1
    for item in outs:
        if outs[item]>r or (len(item)>l and outs[item]>1):
            l=len(item)
            r=outs[item]
            c=item
    return c.split(chr(1))
#print(get_pattern(pattern))

#im = Image.fromarray(maze.astype('uint8')*100)
#im.save("maze" + ".png")



    

