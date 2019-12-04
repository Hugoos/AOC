import math
import numpy as np
import re
name2 = "input/input3.txt" #pentest
f=open(name2)
lines=f.readlines()
quilt = np.zeros((1000,1000))
for line in lines:
    #print(line)
    words = re.findall(r'[0-9]+,[0-9]+',line)
    words2 = re.findall(r'[0-9]+x[0-9]+',line)
    split = words[0].split(',')
    split2 = words2[0].split('x')
    x = int(split[0])
    y = int(split[1])
    w = int(split2[0])
    h = int(split2[1])
    for x2 in range(x, x+w):
        for y2 in range(y, y+h):
            quiltnum = quilt[x2][y2]
            quilt[x2][y2] = quiltnum + 1


#print(np.where(quilt > 1).size)
print((quilt > 1).sum())
print(quilt)
