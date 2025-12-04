import numpy as np
from PIL import Image

def npNicePrint(arr, convertDict=None):
    if not convertDict:
        convertDict = {0: ".", 1: "#"}
    s = ""
    for r in arr:
        for c in r:
            s += convertDict[c]
        s += "\n"
    print(s)

def dictNicePrint(d, convertDict=None):
    # d is something like {(x, y): value, ...}
    if not convertDict:
        convertDict = {0: ".", 1: "#"}

    # find bounds
    xs = [pos[0] for pos in d.keys()]
    ys = [pos[1] for pos in d.keys()]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)

    out = []
    for y in range(min_y, max_y + 1):
        row = []
        for x in range(min_x, max_x + 1):
            v = d.get((x, y), 0)
            row.append(convertDict.get(v, v))
        out.append("".join(row))

    print("\n".join(out))

class grid:
    def __init__(self, size):
        self.size = size
        self.grid = np.zeros(size).astype(int)
    def clear(self):
        self.grid = np.zeros(self.size).astype(int)
    def on(self,p1,p2, binary=True):
        x1,y1 = int(p1[0]), int(p1[1])
        x2,y2 = int(p2[0]), int(p2[1])
        if binary:
            self.grid[x1:x2+1, y1:y2+1] = 1
        else:
            self.grid[x1:x2+1, y1:y2+1] += 1
    def off(self,p1,p2, binary=True):
        x1,y1 = int(p1[0]), int(p1[1])
        x2,y2 = int(p2[0]), int(p2[1])
        
        if binary:
            self.grid[x1:x2+1, y1:y2+1] = 0
        else:
            self.grid[x1:x2+1, y1:y2+1] -= 1   
            self.grid[x1:x2+1, y1:y2+1] = self.grid[x1:x2+1, y1:y2+1].clip(min=0)
    def toggle(self,p1,p2, binary=True):
        x1,y1 = int(p1[0]), int(p1[1])
        x2,y2 = int(p2[0]), int(p2[1])
        sli = self.grid[x1:x2+1, y1:y2+1]
        if binary:
            self.grid[x1:x2+1, y1:y2+1] = np.where((sli==0)|(sli==1), sli^1, sli)
        else:
            self.grid[x1:x2+1, y1:y2+1] += 2
    def toggle_all(self):
        self.grid = np.where((self.grid==0)|(self.grid==1), self.grid^1, self.grid)
    def nPrint(self):
        npNicePrint(self.grid)
    def countOn(self):
        return sum(sum(self.grid))
    def countOff(self):
        return (self.size[0] * self.size[1]) - sum(sum(self.grid))
    def save(self, name):
        im = Image.fromarray(np.uint8(self.grid * 255) , 'L')
        #im = Image.fromarray(self.grid).convert('1')
        im.save(f"{name}.png")

def visualize_dict_grid(coordinate_dict):
    """
    Visualizes a dictionary with (x, y) coordinates as keys and values as the grid content.

    :param coordinate_dict: Dictionary with keys as (x, y) tuples and values as grid values.
    """
    # Find the maximum x and y to determine grid dimensions
    max_x = max(key[0] for key in coordinate_dict.keys())
    max_y = max(key[1] for key in coordinate_dict.keys())
    
    # Create the grid
    grid = [[" " for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    
    # Populate the grid with values from the dictionary
    for (x, y), value in coordinate_dict.items():
        grid[y][x] = str(value)  # Convert values to strings for uniform display

    # Print the grid
    for row in grid:
        print(" ".join(row))

def delete_multiple_element(list_object, indices):
    indices = sorted(indices, reverse=True)
    for idx in indices:
        if idx < len(list_object):
            list_object.pop(idx)
            
def pairwise(iterable):
    "s -> (s0, s1), (s2, s3), (s4, s5), ..."
    a = iter(iterable)
    return zip(a, a)


def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]
