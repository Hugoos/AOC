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

permuDict = {}

for line in sortedlines:
    permuDict[line] = []
    for line2 in sortedlines:
        if 0<line2-line<=3:
            permuDict[line].append(line2)
          
permuDict[sortedlines[-1]] = 1
ansDict = permuDict.copy()


for key, value in sorted(list(permuDict.items()), reverse=True):
    if key == sortedlines[-1]:
        continue
    ans = 0
    for val in value:
        ans += ansDict[val]
    ansDict[key] = ans
print(ansDict[0])
        


        
    
        
    
    

