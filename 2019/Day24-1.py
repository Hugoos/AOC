import math
import numpy as np
name2 = "input/input24.txt" #pentest
f=open(name2)
lines=f.readlines()
#lines = """....#
##..#.
##..##
#..#..
##...."""
convertDict = {"#": 1, ".": 0}
state = np.zeros((5,5))
print(lines)
DX = {'L': -1, 'R': 1, 'U': 0, 'D': 0}
DY = {'L': 0, 'R': 0, 'U': -1, 'D': 1}
directionList = ["U","R","D","L"]

hashList = []

def calcBiodiversity(state):
    bioState = state.copy()
    bioState = bioState.flatten()
    biodiversityRating = 0
    for x, bug in enumerate(bioState):
        if x == 0 and bug == 0:
            continue
        biodiversityRating += (bug*2)**x
    return biodiversityRating
        

def advanceTime(oldstate):
    newstate = oldstate.copy()
    for y, line in enumerate(oldstate):
        for x, bug in enumerate(line):
            bugNum = 0
            for direction in directionList:
                if y+DY[direction] >= 0 and y+DY[direction] <= 4 and x+DX[direction] >= 0 and x+DX[direction] <= 4:
                    bugNum += oldstate[y+DY[direction]][x+DX[direction]]
            #print(bugNum)
            if bug and not bugNum == 1:
                newstate[y][x] = 0        
            elif bug == 0 and (bugNum == 1 or bugNum == 2):
                newstate[y][x] = 1
    return newstate
                

for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if not char == "\n":
            state[y][x] = convertDict[char]
hashList.append(hash(state.tostring()))
while True:
    state = advanceTime(state)
    stateHash = hash(state.tostring())
    if stateHash in hashList:
        print("duplicate found")
        break
    hashList.append(stateHash)
print(state)
print(calcBiodiversity(state))
