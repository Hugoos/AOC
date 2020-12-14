import math
import ast 
from AOCTools import *
import copy
import numpy as np
fileName = "input/input14.txt" #pentest
mem = {}
lines= read_strings(fileName, deliminator=" = ")

def applyMask(num,mask):
    numb = bin(num)[2:].zfill(36)
    appliedMask = ""
    for i,maskb in enumerate(mask):
        if maskb == "X":
            appliedMask += numb[i]
        else:
            appliedMask += maskb
    return int(appliedMask,2)

for line in lines:
    if line[0] == "mask":
        mask = line[1]
    else:
        address = line[0][4:-1]
        mem[address] = applyMask(int(line[1]),mask)

print(sum([y for x,y in mem.items()]))
        
