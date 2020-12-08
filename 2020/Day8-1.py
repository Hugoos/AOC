import math
import ast 
from AOCTools import *
fileName = "input/input8.txt" #pentest

lines= read_strings(fileName)
memory = []
for line in lines:
    memory.append((line.split(" ")[0],int(line.split(" ")[1])))
        
class machine():
    def __init__(self, ptr, acc, memory):
        self.ptr = acc
        self.acc = acc
        self.memory = memory
        self.alreadyVisitedList = set()
        

    def debug(self):
        while True:
            operation = self.memory[self.ptr][0]
            value = self.memory[self.ptr][1]
            self.alreadyVisitedList.add(self.ptr)
            if operation == "acc":
                self.acc += value 
                self.ptr += 1
            elif operation == "jmp":
                self.ptr += value
            elif operation == "nop":
                self.ptr += 1
            if self.ptr in self.alreadyVisitedList:
                print(self.acc)
                break
                
    def run(self):
        while True:
            operation = memory[self.ptr][0]
            value = memory[self.ptr][1]
            if operation == "acc":
                self.acc += value
                self.ptr += 1
            elif operation == "jmp":
                self.ptr += value
            elif operation == "nop":
                self.ptr += 1
            
        

machine = machine(0,0,memory)

machine.debug()
        
    
    

