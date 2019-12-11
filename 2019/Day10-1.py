name2 = "input/input10.txt" #pentest
f=open(name2)
lines=f.readlines()

def dxdy(a1,a2):
    return (a2[0] - a1[0], a2[1] - a1[1])

def manDistance(a1,a2):
    return abs(a1[0]-a2[0]) +abs(a1[1]-a2[1])

lines = """.#..#
.....
#####
....#
...##"""

coordList = []

for y, line in enumerate(lines.split('\n')):
    print(line)
    for x, char in enumerate(line):
        if char == "#":
            coordList.append((x,y))

print(coordList)


for asteroid in coordList:
    print(asteroid)
    distanceDict = {asteroid2: manDistance(asteroid, asteroid2) for asteroid2 in coordList if asteroid != asteroid2}
    print("distanceDict: " + str(distanceDict))
    sortedAsteroids = [k for k, v in sorted(distanceDict.items(), key=lambda item: item[1])]
    print("sortedList: " +str(sortedAsteroids))
    removeList = []
    for asteroid2 in sortedAsteroids:
        if asteroid2 in removeList:
            continue
        dixy = dxdy(asteroid,asteroid2)
        if dixy[0]
        for asteroid3 in sortedAsteroids:
            if asteroid == (4,0) and asteroid2 == (4,2) and asteroid3 == (4,3):
                        print("I see you0")
                        print(removeList)
                        print(dixy)
            if asteroid3 in removeList:
                continue
            if asteroid3 == asteroid2:
                continue
            if asteroid == (0,2) and asteroid2 == (1,2) and asteroid3 == (2,2):
                print("Heya")
                print(dixy)
            x = 1
            y = 1
            #print("asteroid2: " + str(asteroid2))
            #print("dxdy:" + str(dixy))
            #print("asteroid3: " + str(asteroid3))
            zeroTextX = False
            if dixy[0] < 0:
                testX = asteroid2[0] + dixy[0]*x >= asteroid3[0]
            else:
                testX = asteroid2[0] + dixy[0]*x <= asteroid3[0]
            while (testX and not zeroTextX):
                if asteroid == (4,0) and asteroid2 == (4,2) and asteroid3 == (4,3):
                        print("I see you1")
                        print(dixy)
                if dixy[0] == 0:
                    zeroTextX = True
                #print("while loop start")
                #print((x,y))
                #print(dixy[0]*x)
                #print(asteroid3[0])
                y = 1
                zeroTextY = False
                if dixy[1] < 0:
                    testY = asteroid2[1] + dixy[1]*y >= asteroid3[1]
                else:
                    testY = asteroid2[1] + dixy[1]*y <= asteroid3[1]
                while (testY and not zeroTextY):
                    if dixy[1] == 0:
                        zeroTextY = True
                    #print(asteroid2[0]+dixy[0]*x)
                    #print(asteroid3[0])
                    if asteroid == (4,0) and asteroid2 == (4,2) and asteroid3 == (4,3):
                        print("I see you2")
                    if asteroid2[0]+dixy[0]*x == asteroid3[0] and asteroid2[1]+dixy[1]*y == asteroid3[1]:
                        print("removed: " + str(asteroid3))
                        removeList.append(asteroid3)
                    y += 1
                    if dixy[1] < 0:
                        testY = asteroid2[1] + dixy[1]*y >= asteroid3[1]
                    else:
                        testY = asteroid2[1] + dixy[1]*y <= asteroid3[1]
                x += 1
                if dixy[0] < 0:
                    testX = asteroid2[0] + dixy[0]*x >= asteroid3[0]
                else:
                    testX = asteroid2[0] + dixy[0]*x <= asteroid3[0]
    outputAsteroids = [x for x in sortedAsteroids if x not in removeList]
    print("outputList: " +str(outputAsteroids))
    print("los:" + str(len(outputAsteroids)))
                    
