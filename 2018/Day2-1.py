import math
name2 = "input/input2.txt" #pentest
f=open(name2)
lines=f.readlines()
calc = 0
score2Total = 0
score3Total = 0
for line in lines:
    score2 = 0
    score3 = 0
    lineset = set(line)
    for char in lineset:
        if line.count(char) == 2:
            score2 = 1
        if line.count(char) == 3:
            score3 = 1
    score2Total += score2
    score3Total += score3

print(score2Total * score3Total)
            
        
