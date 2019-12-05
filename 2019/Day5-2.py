import math
import csv
import unittest
name2 = "input/input5.txt" #pentest

with open(name2, 'r') as f:
    reader = csv.reader(f)
    data = list(reader)

data = data[0]
data = list(map(int, data))
data_orig = data.copy()

def getvalList(data, pointer, parList):
    valList = []
    for i, par in enumerate(parList):
        if par:
            valList.append(data[pointer+i+1])
        else:
            valList.append(data[data[pointer+i+1]])
    return valList


def runMachine(data, inputList=[1],x=0,y=0):
    pointer_move = 0
    outputList = []
    input1 = inputList[0]
    #print(input1)
    #data[1] = x
    #data[2] = y
    loop = True
    pointer = 0
    while loop:
        #print(data)
        parameterList = '{0:05d}'.format(data[pointer])
        #print(parameterList)
        par3 = int(parameterList[0])
        par2 = int(parameterList[1])
        par1 = int(parameterList[2])
        opcode = int(parameterList[3:])
        #print(par3)
        #print(par2)
        #print(par1)
        #print(opcode)
        #print("pointer " + str(pointer))
        try:
            #print("opcode = " + str(opcode))
            if opcode == 1 or opcode == 2:
                if opcode == 1:
                    operation = "+"
                elif opcode == 2:
                    operation = "*"
                else:
                    print("error")   
                valList = getvalList(data,pointer,[par1,par2])
                data[data[pointer+3]] = eval(str(valList[0])+operation+str(valList[1]))
                pointer_move = 4
            elif opcode == 3:
                data[data[pointer+1]] = input1
                pointer_move = 2
            elif opcode == 4:
                valList = getvalList(data,pointer,[par1])
                outputList.append(valList[0])
                pointer_move = 2
            elif opcode == 5:
                valList = getvalList(data,pointer,[par1,par2])
                if valList[0] != 0:
                    pointer = valList[1]
                    continue
                pointer_move = 3
            elif opcode == 6:
                valList = getvalList(data,pointer,[par1,par2])
                if valList[0] == 0:
                    pointer = valList[1]
                    continue
                pointer_move = 3
            elif opcode == 7:
                valList = getvalList(data,pointer,[par1,par2])
                valList.append(data[pointer+3])
                if valList[0] < valList[1]:
                    data[valList[2]] = 1
                else:
                    data[valList[2]] = 0
                pointer_move = 4
            elif opcode == 8:
                valList = getvalList(data,pointer,[par1,par2])
                valList.append(data[pointer+3])
                if valList[0] == valList[1]:
                    data[valList[2]] = 1
                else:
                    data[valList[2]] = 0
                pointer_move = 4
            elif opcode == 99:
                loop = False
            else:
                return -1
        except Exception as e:
            print(e)
            return outputList
        pointer += pointer_move
    return outputList

print(runMachine(data=data_orig.copy(),inputList = [1]))

class TestMachineMethods(unittest.TestCase):

    def test_hard(self):
        self.assertEqual(runMachine(data=[3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99],inputList=[7]), [999])
        self.assertEqual(runMachine(data=[3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99],inputList=[8]), [1000])
        self.assertEqual(runMachine(data=[3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99],inputList=[100]), [1001])

    def test_positionMode1(self):
        #test_data = [3,9,8,9,10,9,4,9,99,-1,8]
        self.assertEqual(runMachine(data=[3,9,8,9,10,9,4,9,99,-1,8],inputList=[8]), [1])
        
    def test_positionMode2(self):
        #test_data = [3,9,8,9,10,9,4,9,99,-1,8]
        self.assertEqual(runMachine(data=[3,9,8,9,10,9,4,9,99,-1,8],inputList=[100]), [0])

    def test_positionMode3(self):
        #test_data = [3,9,7,9,10,9,4,9,99,-1,8]
        self.assertEqual(runMachine(data=[3,9,7,9,10,9,4,9,99,-1,8],inputList=[7]), [1])
        
    def test_positionMode4(self):
        #test_data = [3,9,7,9,10,9,4,9,99,-1,8]
        self.assertEqual(runMachine(data=[3,9,7,9,10,9,4,9,99,-1,8],inputList=[8]), [0])
        
    def test_immediateMode1(self):
        #test_data = [3,9,8,9,10,9,4,9,99,-1,8]
        self.assertEqual(runMachine(data=[3,3,1108,-1,8,3,4,3,99],inputList=[8]), [1])
        
    def test_immediatMode2(self):
        #test_data = [3,9,8,9,10,9,4,9,99,-1,8]
        self.assertEqual(runMachine(data=[3,3,1108,-1,8,3,4,3,99],inputList=[100]), [0])

    def test_immediatMode3(self):
        #test_data = [3,9,7,9,10,9,4,9,99,-1,8]
        self.assertEqual(runMachine(data=[3,3,1107,-1,8,3,4,3,99],inputList=[7]), [1])
        
    def test_immediatMode4(self):
        #test_data = [3,9,7,9,10,9,4,9,99,-1,8]
        self.assertEqual(runMachine(data=[3,3,1107,-1,8,3,4,3,99],inputList=[8]), [0])
        
    def test_positionJump1(self):
        #test_data = [3,9,8,9,10,9,4,9,99,-1,8]
        self.assertEqual(runMachine(data=[3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9],inputList=[0]), [0])
        
    def test_positionJump2(self):
        #test_data = [3,9,8,9,10,9,4,9,99,-1,8]
        self.assertEqual(runMachine(data=[3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9],inputList=[100]), [1])

    def test_immediatJump1(self):
        #test_data = [3,9,7,9,10,9,4,9,99,-1,8]
        self.assertEqual(runMachine(data=[3,3,1105,-1,9,1101,0,0,12,4,12,99,1],inputList=[0]), [0])
        
    def test_immediatJump2(self):
        #test_data = [3,9,7,9,10,9,4,9,99,-1,8]
        self.assertEqual(runMachine(data=[3,3,1105,-1,9,1101,0,0,12,4,12,99,1],inputList=[100]), [1])

    
if __name__ == '__main__':
    unittest.main()

