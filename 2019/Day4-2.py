import re
r1 = 272091
r2 = 815432
#contain = [str(x) + str(x) for x in range(0,10)]
#print(contain)
counter = 0
for x in range(r1, r2+1):
    add = 1
    r1 = re.findall(r"^(?=[0-9]{6}$)(?=(?:.*([0-9])(?!\1))?([0-9])\2(?!\2))(?:0|1(?!0)|2(?![01])|3(?![0-2])|4(?![0-3])|5(?![0-4])|6(?![0-5])|7(?![0-6])|8(?![0-7])|9(?![0-8]))+$",str(x))
    if len(r1) > 0:
        last = -1
        for char in str(x):
            if int(char) >= last:
                last = int(char)
            else:
                add = 0
        counter += add

print(counter)
        


