import math
name2 = "input/input1.txt" #pentest
f=open(name2)
lines=f.readlines()
for l in lines:
    num = 0
    for i, l2 in enumerate(l):
        if l2 == "(":
            num += 1
        if l2 == ")":
            num -= 1
        if num < 0:
            print(i+1)
            break
        
