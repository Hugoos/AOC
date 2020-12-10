import math
import ast 
from AOCTools import *
fileName = "input/input10.txt" #pentest

lines= read_integers(fileName)
lines.append(0)
num1 = 0
num3 = 1
sortedlines = sorted(lines)
for i in range(len(sortedlines)-1):
    if sortedlines[i+1] - sortedlines[i] == 1:
        num1 += 1
    if sortedlines[i+1] - sortedlines[i] == 3:
        num3 += 1

print(num1,num3, num1*num3)
    
        
    
    

