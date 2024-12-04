import networkx as nx
#import matplotlib.pyplot as plt
name2 = "input/input8.txt" #pentest
f=open(name2)
lines=f.readlines()
DG=nx.DiGraph()
#print(lines)
data = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"
#data = lines[0]
instructions = [int(s) for s in data.split(" ")]
print(instructions)
index = 0
name = 0
def startNode(num):
    global name
    global index
    DG.add_node(name, metadata=[])
    name += 1
    childNodes = instructions[index]
    metaData = instructions[index+1]
    index += 2
    idName = name - 1
    for x in range(childNodes):
        parseNode(idName)
    for x in range(metaData):
        DG.node[idName]["metadata"].append(instructions[index + x])
    index = index + metaData

def parseNode(num):
    global name
    global index
    DG.add_node(name, metadata=[], value=-1)
    DG.add_edge(num, name)
    name += 1
    childNodes = instructions[index]
    metaData = instructions[index+1]
    index += 2
    idName = name - 1
    for x in range(childNodes):
        parseNode(idName)
    for x in range(metaData):
        #print(DG.nodes(data=True))
        DG.node[idName]["metadata"].append(instructions[index + x])
    index = index + metaData

startNode(0)
print(DG.nodes())
print(DG.edges())

sume = 0
for node in DG.nodes():
    sume += sum(DG.node[node]["metadata"])
print(sume)
    
shortestPath = nx.shortest_path_length(DG,0)
print(shortestPath)
#DG.add_nodes_from([first,second])
#DG.add_edge(first, second)
depth = max(shortestPath.iteritems(), key=operator.itemgetter(1))[0]
print(depth)
while depth >= 0:
    break

