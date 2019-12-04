import math
from string import ascii_lowercase
name2 = "input/input5.txt" #pentest
f=open(name2)
polymer = f.readline()
origPolymer = polymer
print(polymer)
replaceDict = {}
for c in ascii_lowercase:
    replaceDict[c+c.upper()] = ""
    replaceDict[c.upper()+c] = ""
prelen = len(polymer)
postlen = -1
while prelen != postlen:
    prelen = len(polymer)
    for substring, replacement in replaceDict.items():
        polymer = polymer.replace(substring, replacement)
    postlen = len(polymer)
charDict = {}
for c in ascii_lowercase:
    polymer = origPolymer
    replaceDict2 = {}
    replaceDict2[c] = ""
    replaceDict2[c.upper()] = ""
    for substring, replacement in replaceDict2.items():
        polymer = polymer.replace(substring, replacement)
    prelen = len(polymer)
    postlen = -1
    while prelen != postlen:
        prelen = len(polymer)
        for substring, replacement in replaceDict.items():
            polymer = polymer.replace(substring, replacement)
        postlen = len(polymer)
    charDict[c] = len(polymer) - 1
    
print(charDict)
print(min(charDict.values()))
