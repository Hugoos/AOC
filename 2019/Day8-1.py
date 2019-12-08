import numpy as np
from operator import itemgetter
name2 = "input/input8.txt" #pentest
f=open(name2)
lines=f.readlines()
#lines = 123456789012

def getNumPixel(image, layer, pixel):
    unique, counts = np.unique(image[layer], return_counts=True)
    countDict = dict(zip(unique, counts))
    if pixel in countDict:
        return(countDict[pixel])
    else:
        return 0

width = 25
height = 6
lines = ''.join(x for x in str(lines) if x.isdecimal())
layer = int((len(str(lines)) / (width * height)))
print(layer)
image = np.zeros((layer, width, height))
ind = 0

for l in range(layer):
    for w in range(width):
        for h in range(height):
            image[l][w][h] = lines[ind]
            ind +=1
    
zeroList = [(getNumPixel(image, l, 0), l) for l in range(layer)]
#print(zeroList)
#print(min(zeroList,key=itemgetter(0))[1])
minLayer = min(zeroList,key=itemgetter(0))[1]   #faster solution
print(minLayer)
print(getNumPixel(image,minLayer,1)*getNumPixel(image,minLayer,2))

