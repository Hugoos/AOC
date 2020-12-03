import math
from AOCTools import *
fileName = "input/input3.txt" #pentest

lines= read_strings(fileName)

location = (0,0)
dydx = (3,1)

def move(location, dydx, modulo):
    return((location[0] + dydx[0]) % modulo, location[1] + dydx[1])

locationList = []

while location[1] < abs(len(lines)):
    locationList.append(lines[location[1]][location[0]])
    location = move(location,dydx,abs(len(lines[0])))

print(locationList.count("#"))

        

