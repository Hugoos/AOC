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
m = 119315717514047
n = 101741582076661
pos = 2020
shuffles = { 'deal with increment ': lambda x,m,a,b: (a*x %m, b*x %m),
         'deal into new stack': lambda _,m,a,b: (-a %m, (m-1-b)%m),
         'cut ': lambda x,m,a,b: (a, (b-x)%m) }
a,b = 1,0
with open('input/input22.txt') as f:
  for s in f.read().strip().split('\n'):
    for name,fn in shuffles.items():
      if s.startswith(name):
        arg = int(s[len(name):]) if name[-1] == ' ' else 0
        a,b = fn(arg, m, a, b)
        break
r = (b * pow(1-a, m-2, m)) % m
print(f"Card at #{pos}: {((pos - r) * pow(a, n*(m-2), m) + r) % m}")
