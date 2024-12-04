import math
from Machine import Machine
from collections import namedtuple
import csv
import numpy as np
from PIL import Image
import random
#import Astar
name2 = "input/input19.txt"

Coordinate = namedtuple("Coordinate", 'x y')
DX = {'L': -1, 'R': 1, 'U': 0, 'D': 0}
DY = {'L': 0, 'R': 0, 'U': -1, 'D': 1}
movementCommand = {'L': 3, 'R': 4, 'U': 1, 'D': 2}
directionList = ["U","R","D","L"]

with open(name2, 'r') as f:
    reader = csv.reader(f)
    data = list(reader)

data = data[0]
data = list(map(int, data))
data_orig = data.copy()

state = np.zeros((100,100))
machine = Machine(data=data.copy())
#machine.setMemory(0,2)
i = 1308
while True:
    #for iy in range(i//3, (i*2)//3):
    #for iy in range(i//2, i//2 + 1):
    for iy in range(int(i * 0.80095238095 * 1), int(i * 0.80095238095 * 1.005)):
        ix = i
        for y in range(iy, 100+iy):
            for x in range(ix, 100+ix):
                machine.setInput([x,y])
                outp = next(machine.run())
                #print(outp)
                outp = outp[0]
                    
                state[y-iy][x-ix] = outp
                outp = next(machine.run())
                #print(outp)
        count = np.count_nonzero(state == 1)
        print("Count: %d x: %d, y: %d" %(count, ix, iy))
        im = Image.fromarray(state.astype('uint8')*255)
        im.save("tractorfield2.png")  
        if count == 10000:
            x = ix
            y = iy
            print(ix * 10000 + iy)
            print(ix)
            print(iy)
            break
    #for ix in range(i//3, (i*2)//3):
    #for ix in range(i//2, i//2 + 1):
        #iy = i
        #for y in range(iy, 100+iy):
        #    for x in range(ix, 100+ix):
        #        machine.setInput([x,y])
        #        outp = next(machine.run())
        #        #print(outp)
        #        outp = outp[0]
        #            
        #        state[y-iy][x-ix] = outp
        #        outp = next(machine.run())
        #        #print(outp)
        #count = np.count_nonzero(state == 1)
        #print("Count: %d x: %d, y: %d" %(count, ix, iy))
        #if count == 10000:
        #    x = ix
        #    y = iy
        #    print(ix * 10000 + iy)
        #    print(ix)
        #    print(iy)
        #    break
    i += 1

im = Image.fromarray(state.astype('uint8')*255)
im.save("tractorfield2.png")    


    

