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

def is_between(a,c,b):
    return distance(a,c) + distance(c,b) == distance(a,b)

def isBetween(a, c, b):
    crossproduct = (c[1] - a[1]) * (b[0] - a[0]) - (c[0] - a[0]) * (b[1] - a[1])

    # compare versus epsilon for floating point values, or != 0 if using integers
    if abs(crossproduct) != 0:
        return False

    dotproduct = (c[0] - a[0]) * (b[0] - a[0]) + (c[1] - a[1])*(b[1] - a[1])
    if dotproduct < 0:
        return False

    squaredlengthba = (b[0] - a[0])*(b[0] - a[0]) + (b[1] - a[1])*(b[1] - a[1])
    if dotproduct > squaredlengthba:
        return False

    return True

def angle(p1, p2):
    return math.atan2(p1.y - p2.y, p1.x - p2.x)


#lines = """.#..#
#.....
#####
#....#
#...##"""

coordList = []

for y, line in enumerate(lines):
    print(line)
    for x, char in enumerate(line):
        if char == "#":
            coordList.append((x,y))

print(coordList)
lenList = []

for asteroid in coordList:
    #print(asteroid)
    distanceDict = {asteroid2: manDistance(asteroid, asteroid2) for asteroid2 in coordList if asteroid != asteroid2}
    #print("distanceDict: " + str(distanceDict))
    sortedAsteroids = [k for k, v in sorted(distanceDict.items(), key=lambda item: item[1])]
    #print("sortedList: " +str(sortedAsteroids))
    removeList = []
    for asteroid2 in sortedAsteroids:
        if asteroid2 in removeList:
            continue
        dixy = dxdy(asteroid,asteroid2)
        for asteroid3 in sortedAsteroids:
            dixy2 = dxdy(asteroid,asteroid3)
            #print(dixy, dixy2)
            if asteroid == (4,0) and asteroid2 == (4,2) and asteroid3 == (4,3):
                        #print("I see you0")
                        #print(removeList)
                        #print(dixy)
                        #print(asteroid2[0])
                        #print(asteroid3[0])
                        print("")
            if asteroid3 in removeList:
                continue
            if asteroid3 == asteroid2:
                continue
            if asteroid2[0]-asteroid[0] == 0 or asteroid3[0]-asteroid[0] == 0:
                if asteroid2[0]-asteroid[0] == 0 and asteroid3[0]-asteroid[0] == 0:
                    if isBetween(asteroid3,asteroid2,asteroid) or isBetween(asteroid,asteroid2,asteroid3):
                        #print(asteroid,asteroid2,asteroid3)
                        #print("0We should remove: " + str(asteroid3))
                        removeList.append(asteroid3)
            elif (((asteroid2[1]-asteroid[1])/(asteroid2[0]-asteroid[0])) == ((asteroid3[1]-asteroid[1])/(asteroid3[0]-asteroid[0]))):
                #if manDistance(asteroid,asteroid2) < manDistance(asteroid,asteroid3) and manDistance(asteroid2,asteroid3) < manDistance(asteroid, asteroid3):
                #print(asteroid,asteroid2,asteroid3)
                if isBetween(asteroid3,asteroid2,asteroid) or isBetween(asteroid,asteroid2,asteroid3):
                    #print(asteroid,asteroid2,asteroid3)
                    #print("We should remove: " + str(asteroid3))
                    removeList.append(asteroid3)
            #print("asteroid2: " + str(asteroid2))
            #print("dxdy:" + str(dixy))
            #print("asteroid3: " + str(asteroid3))
                
    outputAsteroids = [x for x in sortedAsteroids if x not in removeList]
    #print("outputList: " +str(outputAsteroids))
    #print("los:" + str(len(outputAsteroids)))
    lenList.append(len(outputAsteroids))
print(lenList)
print(max(lenList))
                    
