import math
name2 = "input/input1.txt" #pentest
f=open(name2)
lines=f.readlines()
calc = 0
for line in lines:
    calc += int(line)
print(calc)
