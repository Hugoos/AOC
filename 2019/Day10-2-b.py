import math
name2 = "input/input10.txt" #pentest
f=open(name2)
lines=f.readlines()

def dxdy(a1,a2):
    return (a2[0] - a1[0], a2[1] - a1[1])

def manDistance(a1,a2):
    return abs(a1[0]-a2[0]) +abs(a1[1]-a2[1])

def distance(a,b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)


def angle(p1, p2):
    return math.atan2(p1[1] - p2[1], p1[0] - p2[0])
#2*math.pi+

def angle2(p1,p2):
    angle2 = angle(p1,p2)
    #print(angle2)
    if angle2 < 0:
        return(math.pi + abs(angle2))
    else:
        return angle2

print(angle2((0,0),(0,1)))
print(angle2((0,0),(1,1)))
print(angle2((0,0),(1,0)))
print(angle2((0,0),(1,-1)))

print(angle2((0,0),(0,-1)))
print(angle2((0,0),(-1,-1)))
print(angle2((0,0),(-1,0)))
print(angle2((0,0),(-1,1)))
#if 2*math.pi+angle((0,0),(-1,1)) > 2*math.pi+angle((0,0),(0,1)):
#    print(angle((0,0),(1,0)) + 2*math.pi+angle((0,0),(-1,1)) - 2*math.pi+angle((0,0),(0,1)))
#lines = """.#..#
#.....
#####
#....#
#...##"""

coordList = []

for y, line in enumerate(lines):
    #print(line)
    for x, char in enumerate(line):
        if char == "#":
            coordList.append((x,y))

#print(coordList)
lenList = []
angleDict = {}
for asteroid in coordList:
    angleDict[asteroid] = []
    for asteroid2 in coordList:
        if asteroid != asteroid2:
            angleDict[asteroid].append(angle(asteroid,asteroid2))

print(max([len(set(angleList)) for angleList in angleDict.values()]))
            
asteroid = [key for key in angleDict if len(set(angleDict[key])) == 221][0]
print(asteroid)



