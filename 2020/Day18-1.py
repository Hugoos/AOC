import math
import ast 
from AOCTools import *
import copy
import numpy as np
import itertools as it
import re
fileName = "input/input18.csv"
lines = read_strings(fileName)

print(lines)

#test = "2 * 3 + (4 * 5)"
#test = "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"
#test = "2 + 4 * 9"
summetje = 0

print("14".isdigit())
def calcGroup(g):
    operation = "+"
    val = 0
    for x in g:
        if x.isdigit():
            val = eval(str(val) + operation + str(x))
        else:
            operation = x
    return val
ans = 0
for expression in lines:
    while True:
        m = re.search(r"\(([^\(^\)]*)\)", expression)
        if not m:
            break
        val = calcGroup(m.group()[1:-1].split(" "))
        expression = expression.replace(m.group(), str(val))

    ans += int(calcGroup(expression.split(" ")))

print(ans)


    
    
