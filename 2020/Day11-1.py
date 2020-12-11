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
    coords = [(min(x+1,maxX-1),y),(max(x-1,0) ,y),(x,min(maxY-1,y+1)),(x,max(y-1,0)),(min(x+1,maxX-1),min(maxY-1,y+1)),(max(x-1,0) , max(y-1,0)),(max(x-1,0),min(maxY-1,y+1)),(min(x+1,maxX-1),max(y-1,0))]
    coords = [(x2,y2) for x2,y2 in coords if not x == x2 or not y == y2]
    coords = set(coords)
    vals = []
    for x2,y2 in coords:
        vals.append(grid[y2][x2])
    return vals
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
            if val == "#" and numHash >= 4:
                updatedGrid[y][x] = "L"
    if grid == updatedGrid:
        print(k)
        break
    grid = copy.deepcopy(updatedGrid)
    #nicePrintGrid(grid)
        
print(sum(x.count("#") for x in grid))    
        
        

        
    
    

