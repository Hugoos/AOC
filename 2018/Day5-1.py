import math
from string import ascii_lowercase
name2 = "input/input5.txt" #pentest
f=open(name2)
polymer = f.readline()
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
    
print(polymer)
print(len(polymer) - 1)
