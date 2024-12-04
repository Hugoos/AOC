from collections import namedtuple
import numpy as np
import matplotlib.pyplot as plt
name2 = "input/input10.txt" #pentest
f=open(name2)
lines=f.readlines()
serialNumber = 3031
grid = np.ones((300,300))

for y in range(300):
    for x in range(300):
        rackId = (x+1) + 10
        powerLevel = rackId * (y+1) + serialNumber
        powerLevel = powerLevel * rackId
        try:
            digit = int(str(powerLevel)[2])
        except:
            digit = 0 
        grid[y][x] = digit - 5

print(grid)
                
def sum9(grid, middleX, middleY):
    return(sum([grid[y][x] for y in range(middleY - 1, middleY + 2) for x in range(middleX - 1, middleX + 2)]))

summ = 0
for y in range(1, 299):
    for x in range(1, 299):
        score = sum9(grid,x,y)
        if score > summ:
            summ = score
            xans = x
            yans = y
    
print(xans+1, yans+1)    

import numpy as np
from scipy.signal import convolve2d

def convolve(power, k_size):
    k = np.ones((k_size, k_size))
    pool = convolve2d(power, k, 'valid')
    x = np.argmax(pool) // pool.shape[0]
    y = np.argmax(pool) % pool.shape[0]
    val = pool[x,y]

    # Indexing starts from 0
    x += 1
    y += 1
    return x, y, val

def part1(power):
    return convolve(power, 3)

def part2(power):
    best_val = 0
    for ks in range(1, 50):
        x, y, val = convolve(power, ks)
        if val > best_val:
            best_x = x
            best_y = y
            best_ks = ks
            best_val = val
    return best_x, best_y, best_ks, best_val


if __name__ == '__main__':
    serial_number = 3031
    grid = np.meshgrid(range(1,301), range(1,301))
    X = grid[0].T
    Y = grid[1].T

    rack_id = X + 10.
    power = rack_id * Y
    power += serial_number
    power *= rack_id
    power = power // 100 % 10
    power -= 5

    x, y, val = part1(power)
    print('x: {}, y: {}, val: {}'
          .format(x, y, val))

    x, y, kernel_size, val = part2(power)
    print('x: {}, y: {}, ks: {}, val: {}'
          .format(x, y, kernel_size, val))
