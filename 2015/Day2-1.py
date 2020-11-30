import math
name2 = "input/input2.txt" #pentest
f=open(name2)
lines=f.readlines()

def surface(l,w,h):
    return 2*l*w + 2*w*h + 2*h*l

def smallestArea(l,w,h):
    sortedAreaList = sorted([l,w,h])
    return sortedAreaList[0] * sortedAreaList[1]

totalWrappingPaperNeeded = 0
for l in lines:
    l,w,h = l.split("x")
    totalWrappingPaperNeeded += (surface(int(l),int(w),int(h)) + smallestArea(int(l),int(w),int(h)))

print(totalWrappingPaperNeeded)
        
