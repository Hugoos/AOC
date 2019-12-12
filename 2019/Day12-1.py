import math
from collections import namedtuple
import re
name2 = "input/input12.txt" #pentest
f=open(name2)
data=f.readlines()

Position = namedtuple('Position', 'x y z')
Velocity = namedtuple('Velocity', 'x y z')

#data =  """<x=-8, y=-10, z=0>
#<x=5, y=5, z=10>
#<x=2, y=-7, z=3>
#<x=9, y=-8, z=-3>"""

planetList = []

class Planet:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity
        self.positionOriginal = position.copy()
        self.velocityOriginal = velocity.copy()

    def print(self):
        print(self.position, self.velocity)
        print(self.positionOriginal, self.velocityOriginal)

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
        
        
    
        

def dxdy(a1,a2):
    return (a2[0] - a1[0], a2[1] - a1[1])

def manDistance(a1,a2):
    return abs(a1[0]-a2[0]) +abs(a1[1]-a2[1])

def distance(a,b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)


def angle(p1, p2):
    return math.atan2(p1[1] - p2[1], p1[0] - p2[0])

for line in data:
    print(line)
    coords = re.findall("[-\d]+", line)
    print(coords)
    planet = Planet(Position(int(coords[0]),int(coords[1]),int(coords[2])),Velocity(0,0,0))
    planetList.append(planet)

for planet in planetList:
        planet.print()

steps = 1000
for step in range(steps):      
    for planet in planetList:
        for planet2 in planetList:
            if planet is not planet2:
                planet.applyGravity(planet2)
    for planet in planetList:
        planet.applyVelocity()
        planent.print()

print("----")
for planet in planetList:
    planet.print()

totalEnergyList = [planet.totalEnergy() for planet in planetList]

print(totalEnergyList)
print(sum(totalEnergyList))
        
    
