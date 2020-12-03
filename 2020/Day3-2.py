import math
from AOCTools import *
from functools import reduce
fileName = "input/input3.txt" #pentest

lines= read_strings(fileName)

ansList = []
dydxList = [(1,1),(3,1),(5,1),(7,1),(1,2)]

def move(location, dydx, modulo):
    return((location[0] + dydx[0]) % modulo, location[1] + dydx[1])

for dydx in dydxList:
    locationList = []
    location = (0,0)
    while location[1] < abs(len(lines)):
        locationList.append(lines[location[1]][location[0]])
        location = move(location,dydx,abs(len(lines[0])))
    ansList.append(locationList.count("#"))

print(reduce(lambda x, y: x*y, ansList))

        

