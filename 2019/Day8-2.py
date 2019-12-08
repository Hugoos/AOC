import numpy as np
from operator import itemgetter
from PIL import Image

name2 = "input/input8.txt" #pentest
f=open(name2)
lines=f.readlines()
#lines = "0222112222120000"

def getNumPixel(image, layer, pixel):
    unique, counts = np.unique(image[layer], return_counts=True)
    countDict = dict(zip(unique, counts))
    if pixel in countDict:
        return(countDict[pixel])
    else:
        return 0

width = 25 #25
height = 6 #6
lines = ''.join(x for x in str(lines) if x.isdecimal())
layer = int((len(str(lines)) / (width * height)))
#print(layer)
image = np.zeros((layer, height, width))
ind = 0

for l in range(layer):
    for h in range(height):
        for w in range(width):
            image[l][h][w] = lines[ind]
            ind +=1
calcList = []

for h in range(height):
    for w in range(width):
        listje = []
        for l in range(layer):
            listje.append(image[l][h][w])
        calcList.append(listje)
print(calcList)

pixelArray = []
    
for arr in calcList:
    removedList = [value for value in arr if value != 2]
    pixelArray.append(removedList[0])
print(pixelArray)

ind = 0
image = np.zeros((height,width))
for h in range(height):
    for w in range(width):
        image[h][w] = pixelArray[ind]
        ind+=1
print(image)
im = Image.fromarray(image.astype('uint8')*255)
#im = Image.fromarray(image)
#if im.mode != 'RGB':
#    im = im.convert('RGB')
im.save("image.png")


