import math
name2 = "input.txt" #pentest
f=open(name2)
lines=f.readlines()
calc = 0
for line in lines:
    fuel = int(line)
    while fuel >= 0:
        fuel = math.floor(int(fuel) / 3) - 2
        if fuel >= 0:
            calc += fuel

print(calc)
