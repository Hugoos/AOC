import math
import csv
name2 = "input/input5.txt" #pentest

with open(name2, 'r') as f:
    reader = csv.reader(f)
    data = list(reader)

data = data[0]
data = list(map(int, data))
data_orig = data.copy()


def runMachine(inputList=[1],x=0,y=0):
    counter_move = 0
    outputList = []
    data = data_orig.copy()
    #print(data)
    input1 = inputList[0]
    #print(input1)
    #data[1] = x
    #data[2] = y
    loop = True
    index = 0
    while loop:
        parameterList = '{0:05d}'.format(data[index])
        #print(parameterList)
        par3 = int(parameterList[0])
        par2 = int(parameterList[1])
        par1 = int(parameterList[2])
        opcode = int(parameterList[3:])
        #print(par3)
        #print(par2)
        #print(par1)
        #print(opcode)
        #print("index " + str(index))
        try:
            if opcode == 1 or opcode == 2:
                #print("opcode = " + str(opcode))
                if opcode == 1:
                    operation = "+"
                elif opcode == 2:
                    operation = "*"
                else:
                    print("error")
                    
                valList = []
                for i, par in enumerate([par1,par2]):
                    #print(index+i+1)
                    if par:
                        valList.append(data[index+i+1])
                    else:
                        valList.append(data[data[index+i+1]])
                print(valList)
                data[data[index+3]] = eval(str(valList[0])+operation+str(valList[1]))
                print(data[data[index+3]])
                counter_move = 4
            elif opcode == 3:
                data[data[index+1]] = input1
                counter_move = 2
            elif opcode == 4:
                outputList.append(data[data[index+1]])
                counter_move = 2
            elif opcode == 99:
                loop = False
            else:
                return -1
        except:
            return outputList
        index += counter_move
    return outputList

print(runMachine())

#for x in range(100):
#    for y in range(100):
#        #print(runMachine(x,y))
#        if runMachine(x,y) == 19690720:
#            print(100 * x + y)

