import math
import ast
import re
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
listofValidCredentials = []
listofInitialValidCredentials = []
for credentials in listofCredentials:
    credentialsKeys = credentials.keys()
    if len(requiredSet - credentialsKeys) == 0:
        listofInitialValidCredentials.append(credentials)
eyeColorList = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
for initalValidCredential in listofInitialValidCredentials:
    if int(initalValidCredential["byr"]) < 1920 or int(initalValidCredential["byr"]) > 2002:
        continue
    if int(initalValidCredential["iyr"]) < 2010 or int(initalValidCredential["iyr"]) > 2020:
        continue
    if int(initalValidCredential["eyr"]) < 2020 or int(initalValidCredential["eyr"]) > 2030:
        continue
    hgt = initalValidCredential["hgt"]
    if "cm" in hgt:
        hgt = int(hgt.split("cm")[0])
        if hgt <  150 or hgt > 193:
            continue
    elif "in" in hgt:
        hgt = int(hgt.split("in")[0])
        if hgt <  59 or hgt > 76:
            continue
    else:
        print("error parsing height")
        continue
    if not re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', initalValidCredential["hcl"]):
        continue
    if not initalValidCredential["ecl"] in eyeColorList:
        continue
    if not len(initalValidCredential["pid"]) == 9:
        continue
    listofValidCredentials.append(initalValidCredential)

print(len(listofValidCredentials))
    
    
    
    

