import math
from AOCTools import *
fileName = "input/input1.txt" #pentest

lines= read_integers(fileName)
linesSet = set(lines)

for line in lines:
    for line2 in lines:
        if (2020 - (line + line2)) in linesSet:
            print(str(line) + " + " + str(line2) + " + " + str(2020-line) +
                  " together add up to 2020\nTheir product is: "
                  + str(line * line2 * (2020-(line+line2))) + "\n")
            break
        


#ans 49880012
