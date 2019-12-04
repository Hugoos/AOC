import math
from string import ascii_lowercase
name2 = "input/input5.txt" #pentest
f=open(name2)
polymer = f.readline()
#print(polymer)
replaceDict = {}

for c in ascii_lowercase:
    replaceDict[c+c.upper()] = ""
    replaceDict[c.upper()+c] = ""
prelen = len(polymer)
postlen = -1
iteration = 1
while prelen != postlen:
    print("iteration: " + str(iteration))
    prelen = len(polymer)
    stopLoop = False
    for i in range(len(polymer)):
        for substring, replacement in replaceDict.items():
            if substring == polymer[i:i+2]:
                #print(substring)
                #print(polymer[i:i+2])
                #print("hello1")
                polymer = polymer[:i] + polymer[i+2:] 
                #print(polymer[i:i+2])
                stopLoop = True
                break
        if stopLoop:
            #print("hello2")
            break
    #print("I am here")
    postlen = len(polymer)
    iteration += 1
    
print(polymer)
print(len(polymer))
