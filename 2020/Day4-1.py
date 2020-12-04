import math
import ast 
from AOCTools import *
fileName = "input/input4.txt" #pentest

lines= read_strings(fileName, " ")
  
listofCredentials = []
credentialDict = {}

for line in lines:
    if line[0] == "":
        listofCredentials.append(credentialDict)
        credentialDict = {}
        continue    
    for entry in line:
        key = entry.split(":")[0]
        value = entry.split(":")[1]
        credentialDict[key] = value
listofCredentials.append(credentialDict)    

requiredSet = set(("byr","iyr","eyr","hgt","hcl","ecl","pid"))
numValid = 0
for credentials in listofCredentials:
    credentialsKeys = credentials.keys()
    if len(requiredSet - credentialsKeys) == 0:
        numValid += 1
print(numValid)
    
    

