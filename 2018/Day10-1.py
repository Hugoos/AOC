from collections import namedtuple
import numpy as np
import matplotlib.pyplot as plt
name2 = "input/input10.txt" #pentest
f=open(name2)
lines=f.readlines()

Coordinate = namedtuple("Coordinate", 'x y velx vely')

#print(lines)

coordList = []
for line in lines:
    l = line.split("<")
    pos = l[1].split(",")
    posx = int(pos[0])
    posy = int(pos[1].split(">")[0])
    pos2 = l[2].split(",")
    velx = int(pos2[0])
    vely = int(pos2[1].split(">")[0])
    coord = Coordinate(posx,posy,velx,vely)
    coordList.append(coord)
    #print(coord)

def getpoints(coords, time):
    coordList = []
    for coord in coords:
        coordList.append((coord.x + time * coord.velx, coord.y + time * coord.vely))
    plt.scatter([i[0] for i in coordList], [i[1] for i in coordList])
    plt.show()

for x in range(0,100):
    
    print(x)
    getpoints(coordList,10640+x*1)

    
    
