import math
name2 = "input/input1.txt" #pentest
f=open(name2)
lines=f.readlines()
for line in lines:
    for line2 in lines:        
        if int(line) + int(line2) == 2020:
            print(int(line)*int(line2))
