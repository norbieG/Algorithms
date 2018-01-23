#min cut algorithm

import random
import copy

cuts = []
graph_org = {}

for line in open('kargerMinCut.txt'):
	vertex = line.strip().split()
	vertex = map(int, vertex) #map function-useful to convert list of str to ints
	graph_org[vertex[0]] = vertex[1:]

for i in xrange(0,50):
	graph = copy.deepcopy(graph_org)

	while len(graph.keys()) > 2:	
		v1 = random.choice(graph.keys())
		v2 = random.choice(graph[v1])
		#merge both vertices
		graph[v1].extend(graph[v2])
		#change old connections (v2) to the new node(v1)
		for elem in graph[v2]:
		    links = graph[elem]
		    for i in xrange(0, len(links)):    
		        if links[i] == v2:
		            links[i] = v1
		#remove self-loops            
		while graph[v1].count(v1) > 0:
		    graph[v1].remove(v1)
		#remove vertex2    
		graph.pop(v2)
	cuts.append(len(graph[graph.keys()[0]]))

print min(cuts)