import math
from AOCTools import *
fileName = "input/input1.txt" #pentest

lines= read_integers(fileName)
linesSet = set(lines)

for line in lines:
    if (2020 - line) in linesSet:
        print(str(line) + " + " + str(2020-line) +
              " together add up to 2020\nTheir product is: "
              + str(line * (2020-line)))
        break
        

