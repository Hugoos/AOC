import math
import ast 
from AOCTools import *
import copy
fileName = "input/input11.txt" #pentest

lines= read_strings(fileName)
#print(lines)
#lines = ["L.LL.LL.LL",
#"LLLLLLL.LL",
#"L.L.L..L..",
#"LLLL.LL.LL",
#"L.LL.LL.LL",
#"L.LLLLL.LL",
#"..L.L.....",
#"LLLLLLLLLL",
#"L.LLLLLL.L",
#"L.LLLLL.LL"]

grid = []
for line in lines:
    row = []
    for char in line:
        row.append(char)
    grid.append(row)
#print(grid)
#grid[y][x]
def getAdjacent(x,y):
    maxX = len(grid[0])
    maxY = len(grid)
    directions = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,-1),(-1,1)]
    vals = []
    for direction in directions:
        #print(direction)
        for i in range(1,max(maxX,maxY)):
            #print(y+direction[1]*i)
            #print(x+direction[0]*i)
            #print(grid[-1][0])
            #print(grid[y+direction[1]*i][x+direction[0]*i])
            if y+direction[1]*i < 0 or y+direction[1]*i > maxY-1 or x+direction[0]*i < 0 or x+direction[0]*i > maxX-1:
                vals.append(".")
                break
            if not grid[y+direction[1]*i][x+direction[0]*i] == ".":
                vals.append(grid[y+direction[1]*i][x+direction[0]*i])
                break
    return vals

#print(getAdjacent(0,0))
def nicePrintGrid(g):
    for y in g:
        row = ""
        for x in y:
            row += x
        row += "\n"
        print(row)
    print("\n")
k = 0
while True:
    k += 1
    updatedGrid = copy.deepcopy(grid)
    for y,row in enumerate(grid):
        for x,val in enumerate(grid[y]):
            adjacentvals = getAdjacent(x,y)
            numDot = adjacentvals.count(".")
            numHash = adjacentvals.count("#")
            numL = adjacentvals.count("L")           
            if val == "L" and numHash == 0:
                updatedGrid[y][x] = "#"                
            if val == "#" and numHash >= 5:
                updatedGrid[y][x] = "L"
    if grid == updatedGrid:
        print(k)
        break
    grid = copy.deepcopy(updatedGrid)
    #nicePrintGrid(grid)
        
print(sum(x.count("#") for x in grid))    
        
        

        
    
    

