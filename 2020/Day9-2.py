import math
import ast 
from AOCTools import *
fileName = "input/input9.txt" #pentest

lines= read_integers(fileName)

for i in range(len(lines)-25):
    sumList = set([int(x)+int(y) for p,x in enumerate(lines[i:i+25]) for q,y in enumerate(lines[i:i+25]) if not p == q])
    if lines[i+25] not in sumList:
        num = lines[i+25]
        break

for p,x in enumerate(lines):
    numList = [x]
    summetje = x
    #print(lines[p+1:])
    for q,y in enumerate(lines[p+1:]):
        numList.append(y)
        summetje += y
        if summetje > num:
            break
        if summetje == num:
            print(sorted(numList)[0] + sorted(numList)[-1])
            
    

        
    
    

