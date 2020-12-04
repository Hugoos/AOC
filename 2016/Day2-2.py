import math
from AOCTools import *
import numpy as np 
fileName = "input/input2.txt" #pentest

lines= read_strings(fileName)
keypad = [[0,0,1,0,0],[0,2,3,4,0],[5,6,7,8,9],[0,"A","B","C",0],[0,0,"D",0,0]]
directionDict = {"U": np.array([0,-1]), "R": np.array([1,0]), "D": np.array([0,1]), "L": np.array([-1,0])}
#lines =["ULL",
#"RRDDD",
#"LURDL",
#"UUUUD"]
location = np.array([2,2])

def fixOutOfBound(location):
    if location[0] < 0:
        location[0] = 0
    if location[0] > 4:
        location[0] = 4
    if location[1] < 0:
        location[1] = 0
    if location[1] > 4:
        location[1] = 4

def checkinvalid(location):
    return(keypad[location[1]][location[0]] == 0)

password = []
        
for line in lines:
    for direction in line:
        location += directionDict[direction]
        fixOutOfBound(location)
        if checkinvalid(location):
            location -= directionDict[direction]
    password.append(keypad[location[1]][location[0]])
    
print(password)
