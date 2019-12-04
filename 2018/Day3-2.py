import math
import numpy as np
import re
name2 = "input/input3.txt" #pentest
f=open(name2)
lines=f.readlines()
quilt_temp = np.zeros((1000,1000))
num = 1
for line in lines:
    print(num)
    sol = True
    ans = line
    #print(ans)
    words = re.findall(r'[0-9]+,[0-9]+',line)
    words2 = re.findall(r'[0-9]+x[0-9]+',line)
    split = words[0].split(',')
    split2 = words2[0].split('x')
    x = int(split[0])
    y = int(split[1])
    w = int(split2[0])
    h = int(split2[1])
    num2 = 1
    for line2 in lines:
        if num != num2:
            quilt = quilt_temp.copy()
            if (quilt > 1).sum() != 0:
                print("error")
            words3 = re.findall(r'[0-9]+,[0-9]+',line2)
            words4 = re.findall(r'[0-9]+x[0-9]+',line2)
            split3 = words3[0].split(',')
            split4 = words4[0].split('x')
            x3 = int(split3[0])
            y3 = int(split3[1])
            w2 = int(split4[0])
            h2 = int(split4[1])
            for x2 in range(x, x+w):
                for y2 in range(y, y+h):
                    quiltnum = quilt[x2][y2]
                    quilt[x2][y2] = quiltnum + 1
            for x4 in range(x3, x3+w2):
                for y4 in range(y3, y3+h2):
                    quiltnum = quilt[x4][y4]
                    quilt[x4][y4] = quiltnum + 1
            if (quilt > 1).sum() != 0:
                #print("I failed")
                sol = False
                break
        num2 += 1
    if sol:
        print("hey")
        print(num)
    num += 1


#print(np.where(quilt > 1).size)
print((quilt > 1).sum())
print(quilt)
