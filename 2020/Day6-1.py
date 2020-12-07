import math
import ast 
from AOCTools import *
fileName = "input/input6.txt" #pentest

lines= read_strings(fileName, vertDeliminator = " ")
#lines = [["abc"],["a","b","c"],["ab","ac"],["a","a","a","a"],["b"]]
countList = []
for group in lines:
    ansSet = set()
    for ans in group:
        for char in ans:
            ansSet.add(char)
    countList.append(len(ansSet))
print(sum(countList))
    
        

    
    

