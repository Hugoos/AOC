import math
from Machine import Machine
from collections import namedtuple
import csv
import numpy as np
from PIL import Image
import random
name2 = "input/input16.txt"


with open(name2, 'r') as f:
    reader = csv.reader(f)
    data = list(reader)

pattern = [0, 1, 0, -1]



def repeat_to_length(s, wanted):
    return (s * (wanted//len(s) + 1))[:wanted]

def createNewPattern(index, length):
    index = index + 1
    newPattern = [[pattern[0]]*index,[pattern[1]]*index,[pattern[2]]*index,[pattern[3]]*index]
    newPattern = [item for sublist in newPattern for item in sublist]
    old = newPattern.pop(0)
    newPattern.insert(len(newPattern),old)
    newPattern = repeat_to_length(newPattern,length)
    return newPattern

data = data[0][0]
#data = "12345678"
#print(data)

#print(createNewPattern(1, 8))
#print(len(data))
#print(createNewPattern(0,len(data)))
inputVal = data
phases = 100
for z in range(phases):
    ans = ""
    for i, _ in enumerate(inputVal):
        #print(int(str(createNewPattern(i,len(data)))[k])*int(char))
        nPattern = createNewPattern(i,len(inputVal))
        ans += str(sum([nPattern[k]*int(char) for k, char in enumerate(inputVal)]))[-1:]
    inputVal = ans
    
print(inputVal)


#ans = sum([str(sum([createNewPattern(i,len(data))[k]*int(char) for k, char in enumerate(data)]))[-1:] for i in range(len(data))])


