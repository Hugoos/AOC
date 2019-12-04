import math
import numpy as np
import re
import operator
from scipy.sparse import dia_matrix

DX = {'L': -1, 'R': 1, 'U': 0, 'D': 0}
DY = {'L': 0, 'R': 0, 'U': 1, 'D': -1}
coordDict = {}

def writeLine(data):
    coordDist = {}
    steps = 0
    x = 0
    y = 0
    for row in data:
        direction = row[0]
        movement = int(row[1:])
        for _ in range(movement):
            steps += 1
            x += DX[direction]
            y += DY[direction]
            if (x,y) not in coordDist:
                coordDist[(x,y)] = steps
    return coordDist
  
name2 = "input/input3.txt" #pentest
f=open(name2)
A = f.readline()
B = f.readline()
A,B = [x.split(',') for x in [A,B]]
A_list = writeLine(A)
B_list = writeLine(B)
both_list = set(A_list.keys())&set(B_list.keys())
print(min([A_list[val] + B_list[val] for val in both_list]))



