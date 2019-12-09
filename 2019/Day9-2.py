import math
import csv
import unittest
from itertools import permutations 
name2 = "input/input9.txt" #pentest

with open(name2, 'r') as f:
    reader = csv.reader(f)
    data = list(reader)

data = data[0]
data = list(map(int, data))
data_orig = data.copy()


class Machine:
    def __init__(self, data, inputList=[]):
        self.data = data
        self.inputList = inputList
        self.pointer = 0
        self.data_orig = data.copy()
        self.running = False
        self.iterations = 0
        self.relbase = 0
        self.lastOutput = None
        self.debug = False

    def resetData(self):
        self.data = self.data_orig.copy()
        self.pointer = 0

    def updateData(self,data):
        self.data = data
        self.data_orig = data.copy()

    def extendMemory(self,ind):
        if ind >= len(self.data):
            #print("extending memory by " + str(self.pointer+i+1 - len(self.data) + 10))
            self.data = self.data + [0]*(ind - len(self.data) + 10)

    def runMachine(self, inputList=[], debug = False):
        self.debug = debug
        self.running = True
        #print("pointer: " + str(self.pointer))
        if inputList:
            #maybe List errors
            for inp in inputList:
                self.inputList.append(inp)
        pointer_move = 0
        outputList = []
        loop = True
        while loop:
            parameterList = '{0:05d}'.format(self.data[self.pointer])
            par3 = int(parameterList[0])
            par2 = int(parameterList[1])
            par1 = int(parameterList[2])
            opcode = int(parameterList[3:])
            if debug: print("pointer " + str(self.pointer))
            try:
                #print("opcode = " + str(opcode))
                if opcode == 1 or opcode == 2:
                    if opcode == 1:
                        operation = "+"
                    elif opcode == 2:
                        operation = "*"
                    else:
                        print("error")
                    if debug: print("op12")
                    valList = self.getvalList(parList=[[par1,0],[par2,0],[par3,1]])
                    self.data[valList[2]] = eval(str(valList[0])+operation+str(valList[1]))
                    pointer_move = 4
                elif opcode == 3:
                    if debug: print("op3")
                    valList = self.getvalList(parList=[[par1,0]])                    
                    if par1 == 0:
                        self.extendMemory(self.pointer+1)
                        index3 = self.data[self.pointer+1]
                    elif par1 == 1:
                        self.extendMemory(self.pointer+1)
                        index3 = self.data[self.pointer+1]
                    elif par1 == 2:
                        self.extendMemory(self.relbase + self.data[self.pointer+1])
                        index3 = self.relbase + self.data[self.pointer+1]
                    if len(self.inputList) == 0:
                        yield outputList
                    self.data[index3] = self.inputList.pop(0)
                    pointer_move = 2
                elif opcode == 4:
                    if debug: print("op4")
                    valList = self.getvalList(parList=[[par1,0]])
                    if debug: print(valList)
                    outputList.append(valList[0])
                    self.lastOutput = valList[0]
                    #Special code#
                    #self.pointer +=2
                    yield outputList
                    ##############
                    pointer_move = 2
                elif opcode == 5:
                    if debug: print("op5")
                    valList = self.getvalList(parList=[[par1,0],[par2,0]])
                    if valList[0] != 0:
                        self.pointer = valList[1]
                        continue
                    pointer_move = 3
                elif opcode == 6:
                    if debug: print("op6")
                    valList = self.getvalList(parList=[[par1,0],[par2,0]])
                    if valList[0] == 0:
                        self.pointer = valList[1]
                        continue
                    pointer_move = 3
                elif opcode == 7:
                    if debug: print("op7")
                    valList = self.getvalList(parList=[[par1,0],[par2,0],[par3,1]])
                    if valList[0] < valList[1]:
                        self.data[valList[2]] = 1
                    else:
                        self.data[valList[2]] = 0
                    pointer_move = 4
                elif opcode == 8:
                    if debug: print("op8")
                    valList = self.getvalList(parList=[[par1,0],[par2,0],[par3,1]])
                    if valList[2] >= len(self.data):
                        #print("extending memory by " + str(valList[2] - len(self.data) + 1))
                        self.data = self.data + [0]*(valList[2] - len(self.data) + 1)
                    if valList[0] == valList[1]:
                        self.data[valList[2]] = 1
                    else:
                        self.data[valList[2]] = 0
                    pointer_move = 4
                elif opcode == 9:
                    if debug: print("op9")
                    valList = self.getvalList(parList=[[par1,0]])
                    self.relbase += valList[0]
                    pointer_move = 2
                elif opcode == 99:
                    if debug: print("op99")
                    loop = False
                    self.running = False
                    self.iterations += 1
                else:
                    return -1
            except Exception as e:
                print(e)
                return outputList
            self.pointer += pointer_move
        self.resetData()
        yield outputList
    def getvalList(self, parList):
        valList = []
        for i, par in enumerate(parList):
            if par[0] == 1:
                if self.debug: print("position mode")
                if self.pointer+i+3 >= len(self.data):
                    if self.debug: print("extending memory by " + str(abs(self.pointer+i+3 - len(self.data) + 10)))
                    self.data = self.data + [0]*abs((self.pointer+i+3 - len(self.data) + 10))
                if par[1] == 0:
                    valList.append(self.data[self.pointer+i+1])
                elif par[1] == 1:
                    valList.append(self.pointer+i+1)
            elif par[0] == 0:
                if self.debug: print("par 0 mode")
                if self.data[self.pointer+i+1] >= len(self.data):
                    if self.debug: print("extending memory by " + str(abs(self.data[self.pointer+i+1] - len(self.data) + 10)))
                    self.data = self.data + [0]*(abs(self.data[self.pointer+i+1] - len(self.data) + 10))
                if par[1] == 0:
                    valList.append(self.data[self.data[self.pointer+i+1]])
                elif par[1] == 1:
                    valList.append(self.data[self.pointer+i+1])
            elif par[0] == 2:
                if self.debug: print("relative mode")
                if self.relbase + self.data[self.pointer+i+1] >= len(self.data):
                    if self.debug: print("extending memory by " + str(abs(self.relbase + self.data[self.pointer+i+1] - len(self.data) + 10)))
                    self.data = self.data + [0]*(abs(self.relbase + self.data[self.pointer+i+1] - len(self.data) + 10))
                if par[1] == 0:
                    valList.append(self.data[self.relbase + self.data[self.pointer+i+1]])
                elif par[1] == 1:
                    valList.append(self.relbase + self.data[self.pointer+i+1])
        return valList
    def isRunning(self):
        return self.running
    def getIterations(self):
        return self.iterations
    def getLastOutput(self):
        return self.lastOutput
        
m1 = Machine(data.copy())

for x in m1.runMachine([2]):
    print(x)


    

#print(runMachine(data=data_orig.copy(),inputList = [1]))

class TestMachineMethods(unittest.TestCase):

    def test_hard(self):
        #print("starting")
        m1 = Machine(data=[3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99], inputList = [7])
        self.assertEqual(next(m1.runMachine()), [999])
        for x in m1.runMachine():
            continue
        #print("second machine")
        m1.updateData([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99])
        #print("third machine")
        self.assertEqual(next(m1.runMachine([8])), [1000])
        for x in m1.runMachine():
            continue
        #print("fourth machine")
        self.assertEqual(next(m1.runMachine([100])), [1001])

    def test_positionMode1(self):
        #test_data = [3,9,8,9,10,9,4,9,99,-1,8]
        m1 = Machine(data=[3,9,8,9,10,9,4,9,99,-1,8], inputList=[8])
        self.assertEqual(next(m1.runMachine()), [1])
        
    def test_positionMode2(self):
        #test_data = [3,9,8,9,10,9,4,9,99,-1,8]
        m1 = Machine(data=[3,9,8,9,10,9,4,9,99,-1,8], inputList=[100])
        self.assertEqual(next(m1.runMachine()), [0])
        #self.assertEqual(runMachine(data=[3,9,8,9,10,9,4,9,99,-1,8],inputList=[100]), [0])

    def test_positionMode3(self):
        #test_data = [3,9,7,9,10,9,4,9,99,-1,8]
        m1 = Machine(data=[3,9,7,9,10,9,4,9,99,-1,8], inputList=[7])
        self.assertEqual(next(m1.runMachine()), [1])
        #self.assertEqual(runMachine(data=[3,9,7,9,10,9,4,9,99,-1,8],inputList=[7]), [1])
        
    def test_positionMode4(self):
        #test_data = [3,9,7,9,10,9,4,9,99,-1,8]
        m1 = Machine(data=[3,9,7,9,10,9,4,9,99,-1,8], inputList=[8])
        self.assertEqual(next(m1.runMachine()), [0])
        #self.assertEqual(runMachine(data=[3,9,7,9,10,9,4,9,99,-1,8],inputList=[8]), [0])
        
    def test_immediateMode1(self):
        #test_data = [3,9,8,9,10,9,4,9,99,-1,8]
        m1 = Machine(data=[3,3,1108,-1,8,3,4,3,99], inputList=[8])
        self.assertEqual(next(m1.runMachine()), [1])
        #self.assertEqual(runMachine(data=[3,3,1108,-1,8,3,4,3,99],inputList=[8]), [1])
        
    def test_immediatMode2(self):
        #test_data = [3,9,8,9,10,9,4,9,99,-1,8]
        m1 = Machine(data=[3,3,1108,-1,8,3,4,3,99], inputList=[100])
        self.assertEqual(next(m1.runMachine()), [0])
        #self.assertEqual(runMachine(data=[3,3,1108,-1,8,3,4,3,99],inputList=[100]), [0])

    def test_immediatMode3(self):
        #test_data = [3,9,7,9,10,9,4,9,99,-1,8]
        m1 = Machine(data=[3,3,1107,-1,8,3,4,3,99], inputList=[7])
        self.assertEqual(next(m1.runMachine()), [1])
        #self.assertEqual(runMachine(data=[3,3,1107,-1,8,3,4,3,99],inputList=[7]), [1])
        
    def test_immediatMode4(self):
        #test_data = [3,9,7,9,10,9,4,9,99,-1,8]
        m1 = Machine(data=[3,3,1107,-1,8,3,4,3,99], inputList=[8])
        self.assertEqual(next(m1.runMachine()), [0])
        #self.assertEqual(runMachine(data=[3,3,1107,-1,8,3,4,3,99],inputList=[8]), [0])
        
    def test_positionJump1(self):
        #test_data = [3,9,8,9,10,9,4,9,99,-1,8]
        m1 = Machine(data=[3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9], inputList=[0])
        self.assertEqual(next(m1.runMachine()), [0])
        #self.assertEqual(runMachine(data=[3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9],inputList=[0]), [0])
        
    def test_positionJump2(self):
        #test_data = [3,9,8,9,10,9,4,9,99,-1,8]
        m1 = Machine(data=[3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9], inputList=[100])
        self.assertEqual(next(m1.runMachine()), [1])
        #self.assertEqual(runMachine(data=[3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9],inputList=[100]), [1])

    def test_immediatJump1(self):
        #test_data = [3,9,7,9,10,9,4,9,99,-1,8]
        m1 = Machine(data=[3,3,1105,-1,9,1101,0,0,12,4,12,99,1], inputList=[0])
        self.assertEqual(next(m1.runMachine()), [0])
        #self.assertEqual(runMachine(data=[3,3,1105,-1,9,1101,0,0,12,4,12,99,1],inputList=[0]), [0])
        
    def test_immediatJump2(self):
        #test_data = [3,9,7,9,10,9,4,9,99,-1,8]
        m1 = Machine(data=[3,3,1105,-1,9,1101,0,0,12,4,12,99,1], inputList=[100])
        self.assertEqual(next(m1.runMachine()), [1])
        #self.assertEqual(runMachine(data=[3,3,1105,-1,9,1101,0,0,12,4,12,99,1],inputList=[100]), [1])

    
if __name__ == '__main__':
    unittest.main()
