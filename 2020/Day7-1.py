import math
import ast 
from AOCTools import *
fileName = "input/input7.txt" #pentest

lines= read_strings(fileName)
#lines = ["light red bags contain 1 bright white bag, 2 muted yellow bags.",
#"dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
#"bright white bags contain 1 shiny gold bag.",
#"muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
#"shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
#"dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
#"vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
#"faded blue bags contain no other bags.",
#"dotted black bags contain no other bags."]
bagDict = {}
for line in lines:
    tokens = line.split(" ")
    address = tokens[0] + " " + tokens[1]
    if tokens[4] == "no":
        bagDict[address] = ""
        continue
    bagDict[address] = {}
    i = 4
    while i < len(tokens):
        address2 = tokens[i+1] + " " + tokens[i+2]
        bagDict[address][address2] = tokens[i]
        i += 4
#print(bagDict)

target = "shiny gold"
total = 0

def recurseBags(target, bag):
    #print(bag)
    if bag == "":
        return False
    #print(bagDict[bag])
    #print(bag)
    for bag2 in bagDict[bag]:
        #print(bag2)
        if bag2 == target:
            return True
        elif recurseBags(target, bag2) == True:
            return True
    return False
    
for bag in bagDict.keys():
    if recurseBags(target, bag):
        total += 1
print(total)
    
        
    
        

    
    

