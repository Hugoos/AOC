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
#data = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,
#-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,
#53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]
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

    def runMachine(self, inputList=[]):
        self.running = True
        #print("pointer: " + str(self.pointer))
        #print(self.data)
        if inputList:
            #maybe List errors
            for inp in inputList:
                self.inputList.append(inp)
        #print(self.inputList)
        pointer_move = 0
        outputList = []
        #print(input1)
        #data[1] = x
        #data[2] = y
        loop = True
        ##pointer = 0
        while loop:
            #print(data)
            parameterList = '{0:05d}'.format(self.data[self.pointer])
            #print(parameterList)
            par3 = int(parameterList[0])
            par2 = int(parameterList[1])
            par1 = int(parameterList[2])
            opcode = int(parameterList[3:])
            #print("pointer " + str(self.pointer))
            try:
                print("opcode = " + str(opcode))
                if opcode == 1 or opcode == 2:
                    if opcode == 1:
                        operation = "+"
                    elif opcode == 2:
                        operation = "*"
                    else:
                        print("error")
                    #print("op12")
                    valList = self.getvalList(parList=[[par1,0],[par2,0],[par3,1]])
                    print(valList)
                    #print("Hello")
                    print(valList[2])
                    #self.data[self.data[self.pointer+3]] = eval(str(valList[0])+operation+str(valList[1]))
                    self.data[valList[2]] = eval(str(valList[0])+operation+str(valList[1]))
                    pointer_move = 4
                elif opcode == 3:
                    print("op3")
                    print(par1)
                    valList = self.getvalList(parList=[[par1,0]])
                    print(valList)
                    print(self.relbase)
                    
                    if par1 == 0:
                        self.extendMemory(self.pointer+1)
                        index3 = self.data[self.pointer+1]
                    elif par1 == 1:
                        self.extendMemory(self.pointer+1)
                        index3 = self.data[self.pointer+1]
                    elif par1 == 2:
                        self.extendMemory(self.relbase + self.data[self.pointer+1])
                        index3 = self.relbase + self.data[self.pointer+1]
                    print("index3: " + str(index3))
                    if len(self.inputList) == 0:
                        yield outputList
                    self.data[index3] = self.inputList.pop(0)
                    print(self.data[1000])
                    pointer_move = 2
                elif opcode == 4:
                    print("op4")
                    valList = self.getvalList(parList=[[par1,0]])
                    #print(valList[0])
                    outputList.append(valList[0])
                    self.lastOutput = valList[0]
                    #Special code#
                    #self.pointer +=2
                    yield outputList
                    ##############
                    pointer_move = 2
                elif opcode == 5:
                    print("op5")
                    #print(self.data)
                    valList = self.getvalList(parList=[[par1,0],[par2,0]])
                    #print(valList)
                    if valList[0] != 0:
                        self.pointer = valList[1]
                        #print(self.data)
                        continue
                    pointer_move = 3
                    #print(self.data)
                elif opcode == 6:
                    print("op6")
                    valList = self.getvalList(parList=[[par1,0],[par2,0]])
                    if valList[0] == 0:
                        self.pointer = valList[1]
                        continue
                    pointer_move = 3
                elif opcode == 7:
                    print("op7")
                    valList = self.getvalList(parList=[[par1,0],[par2,0],[par3,1]])
                    #valList.append(self.data[self.pointer+3])
                    #print(valList[0])
                    #print(valList[1])
                    #print(valList[2])
                    if valList[0] < valList[1]:
                        self.data[valList[2]] = 1
                    else:
                        self.data[valList[2]] = 0
                    pointer_move = 4
                elif opcode == 8:
                    print("op8")
                    #print(self.data)
                    valList = self.getvalList(parList=[[par1,0],[par2,0],[par3,1]])
                    #valList.append(self.data[self.pointer+3])
                    if valList[2] >= len(self.data):
                        #print("extending memory by " + str(valList[2] - len(self.data) + 1))
                        self.data = self.data + [0]*(valList[2] - len(self.data) + 1)
                    if valList[0] == valList[1]:
                        self.data[valList[2]] = 1
                    else:
                        self.data[valList[2]] = 0
                    pointer_move = 4
                elif opcode == 9:
                    print("op9")
                    valList = self.getvalList(parList=[[par1,0]])
                    print(valList[0])
                    self.relbase += valList[0]
                    print(self.relbase)
                    pointer_move = 2
                elif opcode == 99:
                    #print("op99")
                    loop = False
                    self.running = False
                    self.iterations += 1
                else:
                    return -1
            except Exception as e:
                print(e)
                return outputList
            self.pointer += pointer_move
        #print("your finished")
        self.resetData()
        #print(self.data)
        yield outputList
    def getvalList(self, parList):
        #print("welcome to getvalList")
        valList = []
        for i, par in enumerate(parList):
            if par[0] == 1:
                if self.pointer+i+3 >= len(self.data):
                    #print("extending memory by " + str(self.pointer+i+1 - len(self.data) + 10))
                    self.data = self.data + [0]*(self.pointer+i+3 - len(self.data) + 10)
                #print("position mode")
                #print(self.pointer+i+1)
                #print(len(self.data))
                if par[1] == 0:
                    valList.append(self.data[self.pointer+i+1])
                elif par[1] == 1:
                    valList.append(self.pointer+i+1)
            elif par[0] == 0:
                if self.data[self.pointer+i+3] >= len(self.data):
                    #print("extending memory by " + str(self.data[self.pointer+i+1] - len(self.data) + 10))
                    self.data = self.data + [0]*(self.data[self.pointer+i+3] - len(self.data) + 10)
                #print("par 0 mode")
                if par[1] == 0:
                    valList.append(self.data[self.data[self.pointer+i+1]])
                elif par[1] == 1:
                    valList.append(self.data[self.pointer+i+1])
            elif par[0] == 2:
                if self.relbase + self.data[self.pointer+i+3] >= len(self.data):
                    #print("extending memory by " + str(self.relbase + self.data[self.pointer+i+1] - len(self.data) + 10))
                    self.data = self.data + [0]*(self.relbase + self.data[self.pointer+i+3] - len(self.data) + 10)
                #print("relative mode")
                if par[1] == 0:
                    valList.append(self.data[self.relbase + self.data[self.pointer+i+1]])
                elif par[1] == 1:
                    valList.append(self.relbase + self.data[self.pointer+i+1])
        #print(self.data)
        #print(valList)
        #print("exiting valList")
        return valList
    def isRunning(self):
        return self.running
    def getIterations(self):
        return self.iterations
    def getLastOutput(self):
        return self.lastOutput
        

#data = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
#data = [1,6,7,8,4,8,5,10,0]
#data = [21101,5,10,8,4,8,5,10,0]
#data = [1,6,7,8,4,8,5,10,0]
m1 = Machine(data.copy())
#print(next(m1.runMachine()))\

for x in m1.runMachine([1]):
    print(x)


    

#print(runMachine(data=data_orig.copy(),inputList = [1]))

class TestMachineMethods(unittest.TestCase):

    def test_hard(self):
        #print("starting")
        m1 = Machine(data=[3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99], inputList = [7])
        self.assertEqual(m1.runMachine(), [999])
        #print("second machine")
        m1.updateData([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99])
        #print("third machine")
        self.assertEqual(m1.runMachine([8]), [1000])
        #print("fourth machine")
        self.assertEqual(m1.runMachine([100]), [1001])

    def test_positionMode1(self):
        #test_data = [3,9,8,9,10,9,4,9,99,-1,8]
        m1 = Machine(data=[3,9,8,9,10,9,4,9,99,-1,8], inputList=[8])
        self.assertEqual(m1.runMachine(), [1])
        
    def test_positionMode2(self):
        #test_data = [3,9,8,9,10,9,4,9,99,-1,8]
        m1 = Machine(data=[3,9,8,9,10,9,4,9,99,-1,8], inputList=[100])
        self.assertEqual(m1.runMachine(), [0])
        #self.assertEqual(runMachine(data=[3,9,8,9,10,9,4,9,99,-1,8],inputList=[100]), [0])

    def test_positionMode3(self):
        #test_data = [3,9,7,9,10,9,4,9,99,-1,8]
        m1 = Machine(data=[3,9,7,9,10,9,4,9,99,-1,8], inputList=[7])
        self.assertEqual(m1.runMachine(), [1])
        #self.assertEqual(runMachine(data=[3,9,7,9,10,9,4,9,99,-1,8],inputList=[7]), [1])
        
    def test_positionMode4(self):
        #test_data = [3,9,7,9,10,9,4,9,99,-1,8]
        m1 = Machine(data=[3,9,7,9,10,9,4,9,99,-1,8], inputList=[8])
        self.assertEqual(m1.runMachine(), [0])
        #self.assertEqual(runMachine(data=[3,9,7,9,10,9,4,9,99,-1,8],inputList=[8]), [0])
        
    def test_immediateMode1(self):
        #test_data = [3,9,8,9,10,9,4,9,99,-1,8]
        m1 = Machine(data=[3,3,1108,-1,8,3,4,3,99], inputList=[8])
        self.assertEqual(m1.runMachine(), [1])
        #self.assertEqual(runMachine(data=[3,3,1108,-1,8,3,4,3,99],inputList=[8]), [1])
        
    def test_immediatMode2(self):
        #test_data = [3,9,8,9,10,9,4,9,99,-1,8]
        m1 = Machine(data=[3,3,1108,-1,8,3,4,3,99], inputList=[100])
        self.assertEqual(m1.runMachine(), [0])
        #self.assertEqual(runMachine(data=[3,3,1108,-1,8,3,4,3,99],inputList=[100]), [0])

    def test_immediatMode3(self):
        #test_data = [3,9,7,9,10,9,4,9,99,-1,8]
        m1 = Machine(data=[3,3,1107,-1,8,3,4,3,99], inputList=[7])
        self.assertEqual(m1.runMachine(), [1])
        #self.assertEqual(runMachine(data=[3,3,1107,-1,8,3,4,3,99],inputList=[7]), [1])
        
    def test_immediatMode4(self):
        #test_data = [3,9,7,9,10,9,4,9,99,-1,8]
        m1 = Machine(data=[3,3,1107,-1,8,3,4,3,99], inputList=[8])
        self.assertEqual(m1.runMachine(), [0])
        #self.assertEqual(runMachine(data=[3,3,1107,-1,8,3,4,3,99],inputList=[8]), [0])
        
    def test_positionJump1(self):
        #test_data = [3,9,8,9,10,9,4,9,99,-1,8]
        m1 = Machine(data=[3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9], inputList=[0])
        self.assertEqual(m1.runMachine(), [0])
        #self.assertEqual(runMachine(data=[3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9],inputList=[0]), [0])
        
    def test_positionJump2(self):
        #test_data = [3,9,8,9,10,9,4,9,99,-1,8]
        m1 = Machine(data=[3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9], inputList=[100])
        self.assertEqual(m1.runMachine(), [1])
        #self.assertEqual(runMachine(data=[3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9],inputList=[100]), [1])

    def test_immediatJump1(self):
        #test_data = [3,9,7,9,10,9,4,9,99,-1,8]
        m1 = Machine(data=[3,3,1105,-1,9,1101,0,0,12,4,12,99,1], inputList=[0])
        self.assertEqual(m1.runMachine(), [0])
        #self.assertEqual(runMachine(data=[3,3,1105,-1,9,1101,0,0,12,4,12,99,1],inputList=[0]), [0])
        
    def test_immediatJump2(self):
        #test_data = [3,9,7,9,10,9,4,9,99,-1,8]
        m1 = Machine(data=[3,3,1105,-1,9,1101,0,0,12,4,12,99,1], inputList=[100])
        self.assertEqual(m1.runMachine(), [1])
        #self.assertEqual(runMachine(data=[3,3,1105,-1,9,1101,0,0,12,4,12,99,1],inputList=[100]), [1])

    
if __name__ == '__main__':
    unittest.main()
