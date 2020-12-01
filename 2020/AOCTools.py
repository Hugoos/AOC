def read_integers(filename):
    with open(filename) as f:
        return [int(x) for x in f]
def read_strings(filename):
    with open(filename) as f:
        return [str(x) for x in f]
