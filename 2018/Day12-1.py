from collections import namedtuple
from collections import deque
import numpy as np
import matplotlib.pyplot as plt
name2 = "input/input10.txt" #pentest
f=open(name2)
lines=f.readlines()

data = """initial state: ###....#..#..#......####.#..##..#..###......##.##..#...#.##.###.##.###.....#.###..#.#.##.#..#.#

..### => #
..... => .
..#.. => .
.###. => .
...## => #
#.### => .
#.#.# => #
##..# => .
##.## => #
#...# => .
..##. => .
##.#. => .
...#. => .
#..#. => #
.#### => #
.#..# => #
##... => #
.##.# => .
....# => .
#.... => .
.#.#. => #
.##.. => .
###.# => #
####. => .
##### => #
#.##. => #
.#... => #
.#.## => #
###.. => #
#..## => .
#.#.. => #
..#.# => ."""

changeDict = {}
potDict = {}

initState = data.split("\n")[0].split(": ")[1]
for i, char in enumerate(initState):
    potDict[i] = char

data = data.split("\n")[2:]
for line in data:
    changeDict[line.split(" => ")[0]] = line.split(" => ")[1]



print(potDict)
print(changeDict)

def addPadding(d):
    keys = sorted(d.keys())
    start = keys[0]
    end = keys[-1]
    #print(start, end)
    count = 2
    for i in range(start, start+2):
        if d[i] == "#":
            break
        count -= 1
    for i in range(start - count, start):
        d[i] = "."
    count = 2
    for i in reversed(range(end-1, end+1)):
        #print(i)
        if d[i] == "#":
            break
        count -= 1
    #print(count)
    for i in range(end+1, end+1+count):
        d[i] = "."


def generation(d, d2):
    newd = d.copy()
    for k,v in sorted(d.items()):
        word = ""
        for x in range(k-2,k+3):
            try:
                word += d[x]
            except:
                word += "."
        #print(word)
        for key,val in d2.items():
            if word == key:
                newd[k] = val
    return newd
def printDict(d):
    print(''.join([v for k,v in sorted(d.items())]))
        
print(potDict)
countDict = {}
countDict[0] = sum([k for k,v in potDict.items() if v == "#"])
for i in range(499):
    addPadding(potDict)
    potDict = generation(potDict, changeDict)
    countDict[i+1] = sum([k for k,v in potDict.items() if v == "#"])
#print(potDict)
print(sum([k for k,v in potDict.items() if v == "#"]))
addPadding(potDict)
potDict = generation(potDict, changeDict)
print(sum([k for k,v in potDict.items() if v == "#"]))
#print([countDict[i+1] - countDict[i] for i in range(len(countDict.keys())-1)])

print(17011 + ((50000000000 - 500)* 34)) 
