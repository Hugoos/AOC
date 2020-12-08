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
        self.ptr = ptr
        self.acc = acc
        self.memory = memory
        self.alreadyVisitedList = set()

    def reinit(self):
        self.ptr = 0
        self.acc = 0
        self.alreadyVisitedList = set()
        
    def debug(self):
        self.reinit()
        while self.ptr < len(self.memory):
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
                return False
        return True

    def fixTest(self):
        for i,tup in enumerate(self.memory):
            operation = tup[0]
            value = tup[1]
            if operation == "jmp":
                self.memory[i] = ("nop",value)
                if self.debug():
                    print("Found")
                    return(self.run())
                self.memory[i] = ("jmp",value)
            if operation == "nop":
                self.memory[i] = ("jmp",value)
                if self.debug():
                    print("Found")
                    return(self.run())
                self.memory[i] = ("nop",value)
        return "Not Found"
                
        
                
    def run(self):
        self.reinit()
        while self.ptr < len(self.memory):
            operation = memory[self.ptr][0]
            value = memory[self.ptr][1]
            if operation == "acc":
                self.acc += value
                self.ptr += 1
            elif operation == "jmp":
                self.ptr += value
            elif operation == "nop":
                self.ptr += 1
        return self.acc
            
        

machine = machine(0,0,memory)

print(machine.fixTest())
        
    
    

