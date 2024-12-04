import math
import numpy as np
name2 = "input/input22.txt" #pentest
f=open(name2)
lines=f.readlines()
#lines = """deal into new stack
#cut -2
#deal with increment 7
#cut 8
#cut -4
#deal with increment 7
#cut 3
#deal with increment 9
#deal with increment 3
#cut -1"""
stackSize = 119315717514047
stack = np.arange(stackSize)
#stack = [x for x in range(stackSize)]
print("wow it works")
def newStack(stack):
    stack.reverse()
    return stack

def cut(stack, N):
    stack = stack[N:] + stack[:N]
    return stack

def increment(stack, inc):
    i = 0
    deckSize = len(stack)
    newStack = stack.copy()
    while stack:      
        newStack[i] = stack.pop(0)
        i = (i + inc) % deckSize
    stack = newStack
    return stack
#stack = increment(stack,7)
#stack = newStack(stack)
#stack = newStack(stack)
#print(stack)
for i in range(101741582076661):
    for line in lines:
        #print(line)
        if "deal into new stack" in line:
            #print("dealing stack")
            stack = newStack(stack)
        if "deal with increment" in line:
            inc = int(line.split(" ")[-1])
            #print(inc)
            stack = increment(stack, inc)
        if "cut" in line:
            N = int(line.split(" ")[-1])
            #print(N)
            stack = cut(stack,N)
print(stack[2020])
