import math
import csv
import unittest
from itertools import permutations 
name2 = "input/input7.txt" #pentest

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
    def __init__(self, data, inputList):
        self.data = data
        self.inputList = inputList
        self.pointer = 0
        self.data_orig = data.copy()
        self.running = False
        self.iterations = 0
        self.lastOutput = None

    def resetData(self):
        self.data = self.data_orig.copy()
        self.pointer = 0

    def updateData(self,data):
        self.data = data
        self.data_orig = data.copy()

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
                #print("opcode = " + str(opcode))
                if opcode == 1 or opcode == 2:
                    if opcode == 1:
                        operation = "+"
                    elif opcode == 2:
                        operation = "*"
                    else:
                        print("error")
                    #print("op12")
                    valList = self.getvalList(parList=[par1,par2])
                    #print("Hello")
                    self.data[self.data[self.pointer+3]] = eval(str(valList[0])+operation+str(valList[1]))
                    pointer_move = 4
                elif opcode == 3:
                    #print("op3")
                    if len(self.inputList) == 0:
                        return outputList
                    self.data[self.data[self.pointer+1]] = self.inputList.pop(0)
                    pointer_move = 2
                elif opcode == 4:
                    #print("op4")
                    valList = self.getvalList(parList=[par1])
                    #print(valList[0])
                    outputList.append(valList[0])
                    self.lastOutput = valList[0]
                    #Special code#
                    self.pointer +=2
                    return outputList
                    ##############
                    pointer_move = 2
                elif opcode == 5:
                    #print("op5")
                    #print(self.data)
                    valList = self.getvalList(parList=[par1,par2])
                    #print(valList)
                    if valList[0] != 0:
                        self.pointer = valList[1]
                        #print(self.data)
                        continue
                    pointer_move = 3
                    #print(self.data)
                elif opcode == 6:
                    #print("op6")
                    valList = self.getvalList(parList=[par1,par2])
                    if valList[0] == 0:
                        self.pointer = valList[1]
                        continue
                    pointer_move = 3
                elif opcode == 7:
                    #print("op7")
                    valList = self.getvalList(parList=[par1,par2])
                    valList.append(self.data[self.pointer+3])
                    #print(valList[0])
                    #print(valList[1])
                    #print(valList[2])
                    if valList[0] < valList[1]:
                        self.data[valList[2]] = 1
                    else:
                        self.data[valList[2]] = 0
                    pointer_move = 4
                elif opcode == 8:
                    #print("op8")
                    #print(self.data)
                    valList = self.getvalList(parList=[par1,par2])
                    valList.append(self.data[self.pointer+3])
                    if valList[0] == valList[1]:
                        self.data[valList[2]] = 1
                    else:
                        self.data[valList[2]] = 0
                    pointer_move = 4
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
        return outputList
    def getvalList(self, parList):
        valList = []
        for i, par in enumerate(parList):
            if par:
                #print("if")
                valList.append(self.data[self.pointer+i+1])
            else:
                #print("else")
                #print(self.data[self.pointer+i+1])
                valList.append(self.data[self.data[self.pointer+i+1]])
        #print(self.data)
        #print(valList)
        return valList
    def isRunning(self):
        return self.running
    def getIterations(self):
        return self.iterations
    def getLastOutput(self):
        return self.lastOutput
        

perm = permutations([5,6,7,8,9])

#9,8,7,6,5
#input1 = [0]
#for y in [9,8,7,6,5]:
#    input1 = runMachine(data=data_orig.copy(),inputList = [y, input1[0]])

total = []
for i in perm:
    machine1 = Machine(data=data_orig.copy(), inputList = [i[0]])
    machine2 = Machine(data=data_orig.copy(), inputList = [i[1]])
    machine3 = Machine(data=data_orig.copy(), inputList = [i[2]])
    machine4 = Machine(data=data_orig.copy(), inputList = [i[3]])
    machine5 = Machine(data=data_orig.copy(), inputList = [i[4]])

    input1 = [0]
    while machine5.getIterations() < 1:
        input2 = []
        for put in input1:
            if machine1.getIterations() < 1:
                input2.append(machine1.runMachine([put]))
        input1 = [item for sublist in input2 for item in sublist]
        #print(input1)
        if machine1.getIterations() == 1:
            break
        input2 = []
        for put in input1:
            if machine2.getIterations() < 1:
                input2.append(machine2.runMachine([put]))
        input1 = [item for sublist in input2 for item in sublist]
        #print(input1)
        if machine2.getIterations() == 1:
            break
        input2 = []
        for put in input1:
            if machine3.getIterations() < 1:
                input2.append(machine3.runMachine([put]))
        input1 = [item for sublist in input2 for item in sublist]
        #print(input1)
        if machine3.getIterations() == 1:
            break
        input2 = []
        for put in input1:
            if machine4.getIterations() < 1:
                input2.append(machine4.runMachine([put]))
        input1 = [item for sublist in input2 for item in sublist]
        #print(input1)
        if machine4.getIterations() == 1:
            break
        input2 = []
        for put in input1:
            if machine5.getIterations() < 1:
                input2.append(machine5.runMachine([put]))
        input1 = [item for sublist in input2 for item in sublist]
        #print(input1)
        
    #print("out of the loop")
    total.append(machine5.getLastOutput())


print(max(total))
    

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

