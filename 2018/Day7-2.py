import networkx as nx
#import matplotlib.pyplot as plt
name2 = "input/input7.txt" #pentest
f=open(name2)
lines=f.readlines()
DG=nx.DiGraph()

data = """Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin."""

#for line in data.split("\n"):
for line in lines:
    first = line.split(" ")[1]
    second = line.split(" ")[7]
    DG.add_nodes_from([first,second])
    DG.add_edge(first, second)


word = ""
for x in nx.lexicographical_topological_sort(DG):
    word += x
def getAvailableList(graph):
    availableList = []
    for node in DG.nodes:
        count = 0
        for predecessor in DG.predecessors(node):
            count += 1
        if count == 0:
            availableList.append(node)
    return sorted(availableList)

def getAvailableWorker(workerDict):
    return [key for key in workerDict if workerDict[key]["time"] == 0]


def advanceTime(workerDict, graph):
    for key in workerDict.keys():
        workerDict[key]["time"] = max(workerDict[key]["time"] - 1,0)
        if workerDict[key]["time"] == 0 and workerDict[key]["working"]:
            graph.remove_node(workerDict[key]["working"])
            workerDict[key]["working"] = ""

time = 0
workers = {i:{"time":0,"working":""} for i in range(5)}
while True:
    for worker in getAvailableWorker(workers):
        
        availableNodes = getAvailableList(DG)
        availableNodes = [x for x in availableNodes if x not in [workers[key]["working"] for key in workers.keys()]]
        if availableNodes:
            node = availableNodes[0]
            workers[worker]["time"] = ord(node.lower()) - 96 + 60
            workers[worker]["working"] = node
    if len(getAvailableWorker(workers)) == len(workers.keys()):
        break
    advanceTime(workers, DG)
    time += 1
print("time is " + str(time) + " seconds.")
    
