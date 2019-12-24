import math
from Machine23 import Machine
from collections import namedtuple
import csv
import numpy as np
from PIL import Image
import random
import threading

#import Astar
name2 = "input/input21.txt"
mailbox = {i:[] for i in range(50)}
mailbox[255] = []
print(mailbox)

mutex = threading.Lock()
mutexprint = threading.Lock()
def worker(machine, address):
    print(machine.inputList)
    while True:
        mutex.acquire()
        inp = mailbox[address]
        if mailbox[255]:
            break
        mutex.release()
        if inp:
            machine.setInput(inp)
        else:
            machine.setInput([-1])
        desadd = next(machine.run())
        if desadd == 2:
            print("missing input")
        x = next(machine.run())
        y = next(machine.run())
        mutexprint.acquire()
        print(desadd, x , y)
        if desadd == 1 or x == 1 or y == 1:
            print("finished apparently")
            break
        #print("Add: %d, desadd: %d, x: %d, y: %d" % (address, desadd[0], x[0] , y[0]))
        mutexprint.release()
        desadd = desadd[0]
        x = x[0]
        y = y[0]
        #print(x)
        #print(y)
        
        mutex.acquire()
        if not desadd in mailbox.keys():
            mailbox[desadd] = []
        l = mailbox[desadd]
        l.append([x,y])
        mailbox[desadd] = l
        mutex.release()
    print(mailbox[255])
    
    

Coordinate = namedtuple("Coordinate", 'x y')
DX = {'L': -1, 'R': 1, 'U': 0, 'D': 0}
DY = {'L': 0, 'R': 0, 'U': -1, 'D': 1}
movementCommand = {'L': 3, 'R': 4, 'U': 1, 'D': 2}
directionList = ["U","R","D","L"]
robotMap = ""
#robotMap.append([])

with open(name2, 'r') as f:
    reader = csv.reader(f)
    data = list(reader)

data = data[0]
data = list(map(int, data))
data_orig = data.copy()

threads = []
for i in range(50):
    machines = Machine(data=data.copy())
    machines.setInput([i])
    t = threading.Thread(target=worker, args = [machines, i])
    threads.append(t)
    t.start()
    




    

