import math
from Machine23 import Machine
from collections import namedtuple
import csv
import numpy as np
from PIL import Image
import random
import threading

class NAT:
    def __init__(self):
        self.x = -1
        self.y = -1
        self.lastSent = -1

    def updateMemory(self,x,y):
        self.x = x
        self.y = y

#import Astar
name2 = "input/input23.txt"
mailbox = {i:[] for i in range(50)}
idlebox = [0 for x in range(50)]
mailbox[255] = []
#print(mailbox)

mutex = threading.Lock()
mutexprint = threading.Lock()
mutexidle = threading.Lock()

def overseer(NAT, machineList):
    while True:
        #print("hey")
        mutex.acquire()
        inp = mailbox[255]
        mailbox[255] = []
        for inp2 in inp:
            #print("update memory")
            NAT.updateMemory(inp2[0],inp2[1])
        mutex.release()
        #idleList = [machine.isIdle() for machine in machineList]
        #print(idlebox)
        mutexidle.acquire()
        if not 0 in idlebox:
            #print("resetting")
            mutex.acquire()
            if NAT.y == NAT.lastSent:
                print("finished: " + str(NAT.y))
            NAT.lastSent = NAT.y
            l = mailbox[0]
            l.append([NAT.x,NAT.y])
            mailbox[0] = l
            mutex.release()
            for i, val in enumerate(idlebox):
                idlebox[i] = 0
            #print("hey it works")
            #print(idlebox)
            #break
        mutexidle.release()
            
        
def worker(machine, address):
    #print(machine.inputList)
    idleTimer = 0
    while True:
        mutex.acquire()
        inp = mailbox[address]
        mailbox[address] = []
        #print(mailbox[address])
        mutex.release()
        if inp:
            for inp2 in inp:
                #print(inp2)
                machine.setInput(inp2)
            idleTimer = 0
            mutexidle.acquire()
            idlebox[address] = 0
            mutexidle.release()
        else:
            idleTimer += 1
            machine.setInput([-1])
            if idleTimer >= 5000:
                mutexidle.acquire()
                idlebox[address] = 1
                mutexidle.release()
        desadd = next(machine.run())
        if desadd == 2:
            #print("missing input")
            continue
        x = next(machine.run())
        y = next(machine.run())
        mutexprint.acquire()
        #print(desadd, x , y)
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
machineList = []
for i in range(50):
    machines = Machine(data=data.copy(), inputListInit = [])
    #print(machines.inputList)
    machines.setInput([i])
    machineList.append(machines)
    t = threading.Thread(target=worker, args = [machines, i])
    threads.append(t)
    t.start()

NAT = NAT()
t = threading.Thread(target=overseer, args = [NAT, machineList])
t.start() 




    

