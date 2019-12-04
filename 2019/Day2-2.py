import math
import csv
name2 = "input2.csv" #pentest

with open(name2, 'r') as f:
    reader = csv.reader(f)
    data = list(reader)

data = data[0]
data = list(map(int, data))
data_orig = data.copy()


def runMachine(x,y):
    data = data_orig.copy()
    #print(data)
    data[1] = x
    data[2] = y
    loop = True
    index = 0
    while loop:
        opcode = data[index]
        #print(opcode)
        try:
            if opcode == 1:
                data[data[index+3]] = data[data[index+1]] + data[data[index+2]]
            elif opcode == 2:
                data[data[index+3]] = data[data[index+1]] * data[data[index+2]]
            elif opcode == 99:
                loop = False
            else:
                return -1
        except:
            return -1
        index += 4
    return data[0]

for x in range(100):
    for y in range(100):
        #print(runMachine(x,y))
        if runMachine(x,y) == 19690720:
            print(100 * x + y)

