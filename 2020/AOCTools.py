import numpy as np

def read_integers(filename):
    with open(filename) as f:
        return [int(x) for x in f]
def read_strings(filename, deliminator = "", vertDeliminator =""):
    if deliminator :
        result = []
        with open(filename) as f:
            for line in f:
                result.append([str(x).strip() for x in line.split(deliminator)])
            if vertDeliminator or vertDeliminator.isspace():
                if vertDeliminator.isspace():
                    vertDeliminator = ""
                result2 = result
                result = []
                nestedResult = []
                for line in result2:
                    if line == vertDeliminator:
                        result.append(nestedResult)
                        nestedResult = []
                        continue    
                    nestedResult.append(line)
                result.append(nestedResult)        
            return result
    else:    
        with open(filename) as f:
            result = [str(x).strip() for x in f]
            if vertDeliminator or vertDeliminator.isspace():
                if vertDeliminator.isspace():
                    vertDeliminator = ""
                result2 = result
                result = []
                nestedResult = []
                for line in result2:
                    if line == vertDeliminator:
                        result.append(nestedResult)
                        nestedResult = []
                        continue    
                    nestedResult.append(line)
                result.append(nestedResult)
            return result
def nicePrintGrid(g):
    for y in g:
        row = ""
        for x in y:
            row += x
        row += "\n"
        print(row)
    print("\n")

def convertDegree2Radians(degree):
    return degree * (np.pi/180)

def rotateXY(coords,theta, clockwise = True, degrees = True):
    if clockwise:
        theta = -theta
    if degrees:
        theta = convertDegree2Radians(theta)
    r = np.array(( (np.cos(theta), -np.sin(theta)),
               (np.sin(theta),  np.cos(theta)) ))
    return r.dot(coords)
