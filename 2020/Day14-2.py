import math
import ast 
from AOCTools import *
import copy
import numpy as np
fileName = "input/input14.txt" #pentest
mem = {}
lines= read_strings(fileName, deliminator=" = ")

testQueue = []

def applyMask(num,mask):
    numb = bin(num)[2:].zfill(36)
    appliedMask = ""
    for i,maskb in enumerate(mask):
        if maskb == "1":
            appliedMask += "1"
        elif maskb == "0":
            appliedMask += numb[i]
        else:
            appliedMask += "X"
    queue = [appliedMask]
    finishedList = []
    while not len(queue) == 0:
        val = queue.pop()
        for i,x in enumerate(val):
            if x == "X":
                num1 = str(val)
                num2 = str(val)
                num1 = num1[:i] + '0' + num1[i+1:]
                num2 = num2[:i] + '1' + num2[i+1:]
                if "X" in num1:
                    queue.append(num1)
                    queue.append(num2)
                else:
                    finishedList.append(num1)
                    finishedList.append(num2)
                break
    return [int(x,2) for x in finishedList]

for line in lines:
    if line[0] == "mask":
        mask = line[1]
    else:
        address = line[0][4:-1]
        addressList = applyMask(int(address),mask)
        for add in addressList:
            mem[add] = int(line[1])

print(sum([y for x,y in mem.items()]))
        
