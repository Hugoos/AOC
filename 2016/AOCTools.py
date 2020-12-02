def read_integers(filename):
    with open(filename) as f:
        return [int(x) for x in f]
def read_strings(filename, commas = False):
    if commas:
        with open(filename) as f:
            return [str(x).strip() for x in f.readline().split(',')]
    else:    
        with open(filename) as f:
            return [str(x) for x in f]
