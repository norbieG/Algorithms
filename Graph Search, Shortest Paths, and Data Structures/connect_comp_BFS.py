# connected components algo using BFS
# input: graph
# output: clusters of connected components

from collections import defaultdict
import numpy as np

graph = defaultdict(list)
nodes = set()


def BFS(G, s):
	stack = []
	backtrack = []
	explored[s] = True
	stack.append(s)

	while len(stack) > 0:
		val = stack.pop(0)
		backtrack.append(val)	
		for edge in G[val]:
			if explored[edge] == False:
				explored[edge] = True
				stack.append(edge)

	print backtrack


#build graph
for line in open('tscc.txt'):
	vertex = line.strip().split()
	vertex = map(int, vertex) #map function-useful to convert list of str to ints
	graph[vertex[0]] += vertex[1:]

#get all nodes
for k, v in graph.iteritems():
	for elem in v:
		nodes.add(k)
		nodes.add(elem)

explored = np.zeros(len(nodes)+1, dtype = bool)

for i in xrange(1, len(nodes)):
	if explored[i] == False:
		BFS(graph,i)
