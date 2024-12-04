import networkx as nx
#import matplotlib.pyplot as plt
#name2 = "input/input8.txt" #pentest
#f#=open(name2)
#lines=f.readlines()

from collections import deque, defaultdict
inp = 260321
#inp = 59414
circle = deque([3,7])
circle2 = deque([3,7])
elf1 = 0
elf2 = 1
count = 0
#if "378" in "".join([str(x) for x in circle]):
#    print("heyou")
while True:
    count += 1
    #if count % 10000 == 0:
        #print(count)
    r = circle[elf1] + circle[elf2]
    r = [int(char) for char in str(r)]
    for x in r:
        circle.append(x)
        if len(circle2) == 8:
            circle2.popleft()
            circle2.append(x)
            #print(circle2)
        else:
            circle2.append(x)
    elf1 = (elf1 + 1 + circle[elf1]) % len(circle)
    elf2 = (elf2 + 1 + circle[elf2]) % len(circle)
    try:
        if str(inp) in "".join([str(x) for x in circle2]):
            print(len(circle) - len(str(inp)))
            break
        word = ""
        #for x in range(inp, inp+10):
        #    #print(x)
        #    word += str(circle[x])
        #print(word)
        #break
    except Exception as e:
        if count >= inp:
            print(e)    
        pass



    
