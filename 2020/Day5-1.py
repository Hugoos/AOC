import math
import ast 
from AOCTools import *
fileName = "input/input5.txt" #pentest

lines= read_strings(fileName)
def binaryTraversal(size,instructions):
    L = 0
    R = size-1
    for ins in instructions:
        if ins == "F" or ins == "L":
            R = R - ((R-L + 1) // 2)
        elif ins == "B" or ins == "R":
            L = L + ((R-L + 1) // 2)
    if L == R:
        return L
    else:
        print("error")

idList = []
for line in lines:
    idList.append(binaryTraversal(128,line[:7]) * 8 + binaryTraversal(8,line[7:]))
idList.sort(reverse=True)
print(idList[0])
    
    

