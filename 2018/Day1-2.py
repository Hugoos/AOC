import math
name2 = "input/input1.txt" #pentest
f=open(name2)
lines=f.readlines()
seenList = [0]
calc = 0
loop = True
while loop:
    #print(seenList)
    for line in lines:
        calc += int(line)
        if calc in seenList:
            loop = False
            break
        else:
            seenList.append(calc)
print(calc)
