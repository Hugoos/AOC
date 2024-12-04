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
                    print(asteroid,asteroid2,asteroid3)
                    print("0We should remove: " + str(asteroid3))
                    removeList.append(asteroid3)
            elif (((asteroid2[1]-asteroid[1])/(asteroid2[0]-asteroid[0])) == ((asteroid3[1]-asteroid[1])/(asteroid3[0]-asteroid[0]))):
                print(asteroid,asteroid2,asteroid3)
                print("We should remove: " + str(asteroid3))
                removeList.append(asteroid3)
            x = 1
            #print("asteroid2: " + str(asteroid2))
            #print("dxdy:" + str(dixy))
            #print("asteroid3: " + str(asteroid3))
            zeroTextX = False
            if dixy[0] < 0:
                dx = -1
                testX = asteroid2[0] + dx*x >= asteroid3[0]
            elif dixy[0] > 0:
                dx = 1
                testX = asteroid2[0] + dx*x <= asteroid3[0]
            else:
                dx = 0
                testX = False
                
            if dixy[1] < 0:
                dy = -1
                testY = asteroid2[1] + dy*x >= asteroid3[1]
                
            elif dixy[1] > 0:
                dy = 1
                testY = asteroid2[1] + dy*x <= asteroid3[1]
            else:
                dy = 0
                testY = False
            #print(testX, testY)
            while (testX or testY):
                
                if asteroid == (4,0) and asteroid2 == (4,2) and asteroid3 == (4,3):
                        #print("I see you1")
                        #print(dixy)
                        print("")

                if asteroid == (4,3) and asteroid2 == (2,2) and asteroid3 == (1,0):
                    #print("I see you2")
                    print("")
                if asteroid2[0]+dx*x == asteroid3[0] and asteroid2[1]+dy*x == asteroid3[1]:
                    print("removed: " + str(asteroid3))
                    removeList.append(asteroid3)
                x += 1

                if dx < 0:
                    testX = asteroid2[0] + dx*x >= asteroid3[0]
                elif dx > 0:
                    testX = asteroid2[0] + dx*x <= asteroid3[0]
                else:
                    testX = False
                    
                if dy < 0:
                    testY = asteroid2[1] + dy*x >= asteroid3[1]
                    
                elif dy > 0:
                    testY = asteroid2[1] + dy*x <= asteroid3[1]
                else:
                    testY = False
                
    outputAsteroids = [x for x in sortedAsteroids if x not in removeList]
    #print("outputList: " +str(outputAsteroids))
    print("los:" + str(len(outputAsteroids)))
                    
