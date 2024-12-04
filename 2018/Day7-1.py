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

for line in lines:
    print(line)
    first = line.split(" ")[1]
    second = line.split(" ")[7]
    print(first, second)
    DG.add_nodes_from([first,second])
    DG.add_edge(first, second)


word = ""
for x in nx.lexicographical_topological_sort(DG):
    word += x

print(word)
