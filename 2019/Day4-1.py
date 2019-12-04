r1 = 272091
r2 = 815432
contain = [str(x) + str(x) for x in range(0,10)]
#print(contain)
counter = 0
for x in range(r1, r2+1):
    add = 1
    a = [ss in str(x) for ss in contain]
    if True in a:
        last = -1
        for char in str(x):
            if int(char) >= last:
                last = int(char)
            else:
                add = 0
        counter += add

print(counter)
        

