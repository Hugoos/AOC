import math
from collections import namedtuple
import re
name2 = "input/input12.txt"
f=open(name2)
data=f.readlines()

Position = namedtuple('Position', 'x y z')
Velocity = namedtuple('Velocity', 'x y z')

planetList = []

class Planet:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity
        self.positionOriginal = position
        self.velocityOriginal = velocity

    def print(self):
        print(self.position, self.velocity)

    def totalEnergy(self):
        potentialEnergy = abs(self.position.x) + abs(self.position.y) + abs(self.position.z)
        kineticEnergy = abs(self.velocity.x) + abs(self.velocity.y) + abs(self.velocity.z)
        totalEnergy = potentialEnergy * kineticEnergy
        return totalEnergy

    def applyVelocity(self):
        self.position = Position(self.position.x + self.velocity.x, self.position.y + self.velocity.y, self.position.z + self.velocity.z)

    def applyGravity(self, planet):
        coordList = []
        for i, coord in enumerate(self.position):
            if coord != planet.position[i]:
                if coord < planet.position[i]:
                    coordList.append(1)
                else:
                    coordList.append(-1)
            else:
                coordList.append(0)
        self.velocity = Velocity(self.velocity.x + coordList[0], self.velocity.y + coordList[1], self.velocity.z + coordList[2])
        
    def checkSame(self):
        xSame = self.position.x == self.positionOriginal.x and self.velocity.x == self.velocityOriginal.x
        ySame = self.position.y == self.positionOriginal.y and self.velocity.y == self.velocityOriginal.y
        zSame = self.position.z == self.positionOriginal.z and self.velocity.z == self.velocityOriginal.z
        return [xSame, ySame, zSame]
        

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

for line in data:
    coords = re.findall("[-\d]+", line)
    planet = Planet(Position(int(coords[0]),int(coords[1]),int(coords[2])),Velocity(0,0,0))
    planetList.append(planet)

for planet in planetList:
        planet.print()
transDict = {0: "x", 1: "y", 2: "z"}
ansDict = {"x": 0,"y": 0, "z": 0}
steps = 1
loop = True
print("----")
while loop:
    for planet in planetList:
        for planet2 in planetList:
            if planet is not planet2:
                planet.applyGravity(planet2)
    positionList = []
    for planet in planetList:
        planet.applyVelocity()
        positionList.append(planet.checkSame())
    for i in range(3):
        if positionList[0][i] and positionList[1][i] and positionList[2][i] and positionList[3][i] and ansDict[transDict[i]] == 0:
            print("found " + str(transDict[i]) + " in " + str(steps) + " steps")
            ansDict[transDict[i]] = steps
            if ansDict["x"] > 0 and ansDict["y"] > 0 and ansDict["z"] > 0:
                loop = False
                break
    steps += 1

print("----")
for planet in planetList:
    planet.print()

totalEnergyList = [planet.totalEnergy() for planet in planetList]

print(totalEnergyList)
print(sum(totalEnergyList))
print("----")
print("lcm is " + str(lcm(lcm(ansDict["x"],ansDict["y"]), ansDict["z"])))
        
    
