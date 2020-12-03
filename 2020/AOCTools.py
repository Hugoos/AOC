def read_integers(filename):
    with open(filename) as f:
        return [int(x) for x in f]
def read_strings(filename, deliminator = ""):
    if deliminator :
        result = []
        with open(filename) as f:
            for line in f:
                result.append([str(x).strip() for x in line.split(deliminator)])
            return result
    else:    
        with open(filename) as f:
            return [str(x).strip() for x in f]
