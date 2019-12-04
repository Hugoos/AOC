import math
import csv
name2 = "input2.csv" #pentest

with open(name2, 'r') as f:
    reader = csv.reader(f)
    data = list(reader)

data = data[0]
data = list(map(int, data))
index = 0
loop = True

data[1] = 12
data[2] = 2

while loop:
    opcode = data[index]
    #print(opcode)
    if opcode == 1:
        data[data[index+3]] = data[data[index+1]] + data[data[index+2]]
    elif opcode == 2:
        data[data[index+3]] = data[data[index+1]] * data[data[index+2]]
    elif opcode == 99:
        loop = False
    else:
        print("ERROR")
    index += 4

print(data[0])

