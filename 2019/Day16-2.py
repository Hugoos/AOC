import math
from Machine import Machine
from collections import namedtuple
import csv
import numpy as np
from PIL import Image
import random
from itertools import cycle, accumulate

def level2():
    with open("input/input16.txt") as f:
        s = f.read().strip()
    offset = int(s[:7])
    digits = [int(i) for i in s]
    # If `rep` is `digits` repeated 10K times, construct: 
    #     arr = [rep[-1], rep[-2], ..., rep[offset]]
    l = 10000 * len(digits) - offset
    i = cycle(reversed(digits))
    arr = [next(i) for _ in range(l)]
    # Repeatedly take the partial sums mod 10
    for _ in range(100):
        arr = [n % 10 for n in accumulate(arr)]
    return "".join(str(i) for i in arr[-1:-9:-1])
name2 = "input/input16.txt"
print(level2())

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
offsetmessage = int(data[:7])
print(offsetmessage)
data = [data * 10000]
print("done")
data = [item for sublist in data for item in sublist]
#data = "12345678"
print("done")

def generateOutputSignal(inp):
    outp = ""
    val = 0
    for char in inp[::-1]:
        val += int(char)
        outp = str((val % 10)) + outp
    return outp

print(generateOutputSignal("12345678"))



#print(createNewPattern(1, 8))
#print(len(data))
#print(createNewPattern(0,len(data)))
inputVal = data
phases = 100
nPattern = [1,0,-1,0]
#for i, _ in enumerate(inputVal):
#    nPattern[i] = createNewPattern(i,len(inputVal))

#print(nPattern[
             
#print("done")
for z in range(phases):
    print("phase " + str(z+1))
    ans = ""
    for i, _ in enumerate(inputVal):
        #print(int(str(createNewPattern(i,len(data)))[k])*int(char))
        #nPattern = createNewPattern(i,len(inputVal))
        ans += str(sum([nPattern[(k//(i+1))%4]*int(char) for k, char in enumerate(inputVal[i:])]))[-1:]
    inputVal = ans
#print(inputVal)    
print(inputVal[offsetmessage:offsetmessage+8])
#ans = sum([str(sum([createNewPattern(i,len(data))[k]*int(char) for k, char in enumerate(data)]))[-1:] for i in range(len(data))])


