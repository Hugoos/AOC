import math
import ast 
from AOCTools import *
fileName = "input/input6.txt" #pentest

lines= read_strings(fileName, vertDeliminator = " ")
#lines = [["abc"],["a","b","c"],["ab","ac"],["a","a","a","a"],["b"]]
countList = []
for group in lines:
    ansSet = set(map(chr, range(97, 123)))
    for ans in group:
        ansSet2 = set()
        for char in ans:
            ansSet2.add(char)
        ansSet = ansSet.intersection(ansSet2)
    countList.append(len(ansSet))
print(sum(countList))
    
        

    
    

