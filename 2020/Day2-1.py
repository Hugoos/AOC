import math
from AOCTools import *
fileName = "input/input2.txt" #pentest

lines= read_strings(fileName, deliminator = " ")
numValid = 0
for line in lines:
    passRange = line[0]
    passChar = line[1].split(":")[0]
    password = line[2]
    passRangeStart = passRange.split("-")[0]
    passRangeEnd = passRange.split("-")[1]
    charsInPass = password.count(passChar)
    if charsInPass >= int(passRangeStart) and charsInPass <= int(passRangeEnd):
        numValid += 1
print(numValid)
    
        

