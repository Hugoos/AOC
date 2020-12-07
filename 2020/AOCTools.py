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
                print("hello")
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
