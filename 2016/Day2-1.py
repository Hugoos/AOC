import math
from AOCTools import *
import numpy as np 
fileName = "input/input2.txt" #pentest

lines= read_strings(fileName)
keypad = [[1,2,3],[4,5,6],[7,8,9]]
directionDict = {"U": np.array([0,-1]), "R": np.array([1,0]), "D": np.array([0,1]), "L": np.array([-1,0])}
#lines =["ULL",
#"RRDDD",
#"LURDL",
#"UUUUD"]
location = np.array([1,1])

def fixOutOfBound(location):
    if location[0] < 0:
        location[0] = 0
    if location[0] > 2:
        location[0] = 2
    if location[1] < 0:
        location[1] = 0
    if location[1] > 2:
        location[1] = 2

password = []
        
for line in lines:
    for direction in line:
        location += directionDict[direction]
        fixOutOfBound(location)
    password.append(keypad[location[1]][location[0]])
    
print(password)
