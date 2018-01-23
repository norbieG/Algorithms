# topological sort algorithm
# for loop and DFS used to show dependencies
# input: graph
# output: topological order of vertices

from collections import defaultdict
import numpy as np

graph = defaultdict(list)
nodes = set()

#build graph
for line in open('top.txt'):
	vertex = line.strip().split()
	vertex = map(int, vertex) #map function-useful to convert list of str to ints
	graph[vertex[0]] += vertex[1:]

#collect nodes
for k, v in graph.iteritems():
	for elem in v:
		nodes.add(k)
		nodes.add(elem)
		
#for every key in dict, use the corresponding value in dict for comparison to sort it
def sort_dict_by_vals(dictionary):
	return sorted(dictionary, key=dictionary.__getitem__)

def DFS(G, s):
	global current_label
	stack = []
	backtrack = []
	explored[s] = True
	stack.append(s)
	print 's', s
	while len(stack) > 0:
		val = stack.pop()
		backtrack.append(val)	
		for edge in G[val]:
			if explored[edge] == False:
				DFS(G, edge)

	while len(backtrack) > 0:
		topology[backtrack.pop()] = current_label
		current_label -=1	

topology = {}
current_label = len(nodes) 
explored = np.zeros(len(nodes), dtype = bool)

for i in xrange(0, len(nodes)):	#assumes node 0
	if explored[i] == False:
		DFS(graph,i)

print 'topological order is: ',sort_dict_by_vals(topology)
