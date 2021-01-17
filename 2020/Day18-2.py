import math
import ast 
from AOCTools import *
import copy
import numpy as np
import itertools as it
import re
fileName = "input/input18.csv"
lines = read_strings(fileName)

def addBrackets(test):
    while "+" in test:
        newTest = test
        for i,x in enumerate(test):
            if x == "+":
                newTest = newTest[:i] + "$" + newTest[i+1:]
                stack = 0
                seenDigit = False
                done = False
                for z in range(i,0,-1):
                    if test[z] == ")" and not seenDigit:
                        stack += 1
                    elif test[z] == "(" and not seenDigit:
                        stack -= 1
                        if stack == 0:
                            newTest = newTest[:z+1] + "(" + newTest[z+1:]
                            done = True
                            break
                    elif test[z].isdigit() and not seenDigit and stack == 0:
                        seenDigit = True
                    elif test[z] == " " and seenDigit and stack == 0:
                        newTest = newTest[:z+1] + "(" + newTest[z+1:]
                        done = True
                        break
                if not done:
                    newTest = "(" + newTest
                stack = 0
                seenDigit = False
                done = False
                for z in range(i,len(test)):
                    if test[z] == "(" and not seenDigit:
                        stack += 1
                    elif test[z] == ")" and not seenDigit:
                        stack -= 1
                        if stack == 0:
                            newTest = newTest[:z+1] + ")" + newTest[z+1:]
                            done = True
                            break
                    elif test[z].isdigit() and not seenDigit and stack == 0:
                        seenDigit = True
                    elif test[z] == " " and seenDigit and stack == 0:
                        newTest = newTest[:z+1] + ")" + newTest[z+1:]
                        done = True
                        break
                if not done:
                    newTest = newTest + ")"
                #print(newTest)
                break
        test = newTest
    return test.replace("$", "+")

    
summetje = 0
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
    expression = addBrackets(expression)
    while True:
        m = re.search(r"\(([^\(^\)]*)\)", expression)
        if not m:
            break
        val = calcGroup(m.group()[1:-1].split(" "))
        expression = expression.replace(m.group(), str(val))

    ans += int(calcGroup(expression.split(" ")))

print(ans)

    
