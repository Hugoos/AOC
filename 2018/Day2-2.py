import math
name2 = "input/input2.txt" #pentest
f=open(name2)
lines=f.readlines()

def funct():
    for line in lines:
        for line2 in lines:
            sumline = 0
            for index, char in enumerate(line):
                if line[index] != line2[index]:
                    sumline += 1
            if sumline == 1:
                print(line)
                print(line2)
                return(line, line2)

print(funct())
                
    
            
        
