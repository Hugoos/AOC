import math
import ast 
from AOCTools import *
fileName = "input/input9.txt" #pentest

lines= read_integers(fileName)

for i in range(len(lines)-25):
    sumList = set([int(x)+int(y) for p,x in enumerate(lines[i:i+25]) for q,y in enumerate(lines[i:i+25]) if not p == q])
    if lines[i+25] not in sumList:
        print(lines[i+25])

        
    
    

