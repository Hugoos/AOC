import math
import pandas as pd
import re
import operator
name = "input/input4.csv" #pentest
data = pd.read_csv(name, header=None)
#print(data)
guardDict = {}
i = 0
while i < len(data[1]):
    line = data[1][i]
    if "#" in line:
        words = re.findall(r'#([0-9]+)',line)
        currId = int(words[0])
        if currId not in guardDict:
            guardDict[currId] = {}
            guardDict[currId]["total"] = 0
            guardDict[currId]["sleepStart"] = []
            guardDict[currId]["sleepEnd"] = []
    line2 = data[1][i+1]
    if "#" in line2:
        i = i+1
        continue
    if "#" in line:
        sleepstart = data[0][i+1]
        sleepend = data[0][i+2]
        i = i+3
    else:
        sleepstart = data[0][i]
        sleepend = data[0][i+1]
        i = i+2
    guardDict[currId]["total"] = guardDict[currId]["total"] + (sleepend - sleepstart)
    #print(guardDict[currId]["sleepStart"])
    guardDict[currId]["sleepStart"].append(sleepstart)
    guardDict[currId]["sleepEnd"].append(sleepend)
    #print(guardDict[currId]["sleepStart"])
    
minDict = {}
ansDict = {}
for key in guardDict.keys():
    sleepStartList = guardDict[key]["sleepStart"]
    sleepEndList = guardDict[key]["sleepEnd"]
    minDict = {}
    #print(sleepStartList)
    #print(sleepEndList)
    for i, stuff in enumerate(sleepEndList):
        for q in range(sleepStartList[i],sleepEndList[i]):
            if q not in minDict:
                minDict[q] = 0
            minDict[q] = minDict[q] + 1
    try:
        ansDict[key] = max(minDict.items(), key=operator.itemgetter(1))[1]
    except:
        continue

print(ansDict)
#print(max(minDict.items(), key=operator.itemgetter(1))[0])
