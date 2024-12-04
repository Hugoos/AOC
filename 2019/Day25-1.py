import math
from Machine import Machine
from collections import namedtuple
import csv
import numpy as np
from PIL import Image
import random
#import Astar
name2 = "input/input25.txt"
#inp = input()
def printMap(robotMap):
    for s in robotMap:
        print(*s)

Coordinate = namedtuple("Coordinate", 'x y')
DX = {'L': -1, 'R': 1, 'U': 0, 'D': 0}
DY = {'L': 0, 'R': 0, 'U': -1, 'D': 1}
movementCommand = {'L': 3, 'R': 4, 'U': 1, 'D': 2}
directionList = ["U","R","D","L"]
robotMap = ""
#robotMap.append([])

with open(name2, 'r') as f:
    reader = csv.reader(f)
    data = list(reader)

data = data[0]
data = list(map(int, data))
data_orig = data.copy()

state = np.zeros((21,42))
machine = Machine(data=data.copy())
#machine.setMemory(0,2)

input_instructions = [",".join([str(x) for x in [ord('N'), ord('O'), ord('T'), ord(' '), ord('A'), ord(' '), ord('J'), ord('\n')]]),
                      
                      ",".join([str(x) for x in [ord('N'), ord('O'), ord('T'), ord(' '), ord('C'), ord(' '), ord('T'), ord('\n')]]),
                      ",".join([str(x) for x in [ord('A'), ord('N'), ord('D'), ord(' '), ord('H'), ord(' '), ord('T'), ord('\n')]]),
                      ",".join([str(x) for x in [ord('O'), ord('R'), ord(' '), ord('T'), ord(' '), ord('J'), ord('\n')]]),
                      
                      ",".join([str(x) for x in [ord('N'), ord('O'), ord('T'), ord(' '), ord('B'), ord(' '), ord('T'), ord('\n')]]),
                      ",".join([str(x) for x in [ord('A'), ord('N'), ord('D'), ord(' '), ord('A'), ord(' '), ord('T'), ord('\n')]]),
                      ",".join([str(x) for x in [ord('A'), ord('N'), ord('D'), ord(' '), ord('C'), ord(' '), ord('T'), ord('\n')]]),
                      ",".join([str(x) for x in [ord('O'), ord('R'), ord(' '), ord('T'), ord(' '), ord('J'), ord('\n')]]),

                      ",".join([str(x) for x in [ord('A'), ord('N'), ord('D'), ord(' '), ord('D'), ord(' '), ord('J'), ord('\n')]]),
                      
                      ",".join([str(x) for x in [ord('R'), ord('U'), ord('N'), ord('\n')]])]
print(input_instructions)

while True:
    outp = next(machine.run())
    #print(outp)
    if outp == 1:
        print("finished")
        print(robotMap)
        break
    if outp == 2:
        #print("asking input")
        #printMap(robotMap)
        print(robotMap)
        #machine.setInput(inputList[indexInput])
        inp = input()
        instructionS = [",".join([str(ord(x)) for x in inp + '\n'])]
        instruction = [int(word) for word in instructionS[0].split(",")]
        #print(instruction)
        machine.setInput(instruction)
        robotMap = ""
        continue
    #print(outp)
    robotMap = robotMap + chr(outp[0])


#im = Image.fromarray(maze.astype('uint8')*100)
#im.save("maze" + ".png")



    

