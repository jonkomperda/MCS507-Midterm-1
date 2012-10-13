import networkx as nx
import numpy
import problem3
#import matplotlib.pyplot as plt

G = nx.Graph()

a = numpy.array([[0,0,0,0,1],[1,0,1,0,0],[0,1,0,1,1],[0,0,1,0,1],[1,0,1,1,0]])
cons = []
for i in range(len(a)):
    for j in range(i,len(a)):
        if a[i,j]==1:
            cons.append((i,j))
#print cons

G.add_edges_from(cons)
paths = nx.all_simple_paths(G, source=0, target=2, cutoff=3)
paths = list(paths)
print paths
for item in paths:
    for x in range(len(item)):
        print item[x]