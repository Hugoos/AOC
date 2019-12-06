import math
name2 = "input/input6.txt" #pentest
f=open(name2)
lines=f.readlines()
orbitDict = {}
class Node(object):
    def __init__(self, data, depth):
        self.data = data
        self.depth = depth
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)


def parseInput(x):
    parent,child = x.split(")")
    return parent,child

def getChecksum(parent, depth):
    checksum = 0
    if parent in orbitDict:
        for child in orbitDict[parent]:
            checksum += getChecksum(child, depth+1)
    checksum += depth
    return checksum

for line in lines:
    parent,child = parseInput(line)
    if not parent in orbitDict.keys():
        orbitDict[parent] = []
    orbitDict[parent].append(child.rstrip())

print(getChecksum("COM", 0))
    
    
