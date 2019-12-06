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

def search(current, last, depth, goal):
    #print(current)
    if current == goal:
        return depth
    for parent in orbitDict.keys():
        if current in orbitDict[parent]:
            if last != parent:
                ans = search(parent, current, depth+1, goal)
                if ans:
                    print(ans - 2)
    if current in orbitDict:
        for child in orbitDict[current]:
            if last != child:
                ans = search(child, current, depth+1, goal)
                if ans:
                    print(ans-2)
            
    


#for parent in orbitDict.keys():
#    if "YOU" in orbitDict[parent]:
#        print(parent)
#        start = parent
#    if "SAN" in orbitDict[parent]:
#        print(parent)
#        end = parent

#print(getChecksum("COM", 0))
print(search("YOU","",0,"SAN"))
    
    
