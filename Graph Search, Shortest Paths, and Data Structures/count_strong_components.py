# Kusaraju algorithm
# input: graph and transposed graph
# call twice dfs on them
# output: count of strongly connected components (SCCs)

import time
start_time = time.time()
from collections import defaultdict
import numpy as np



def DFS(G, s):
	global t
	stack = []
	backtrack = []
	explored[s] = True
	stack.append(s)

	while len(stack) > 0:
		val = stack.pop()
		backtrack.append(val)	


		for edge in G[val]:
			if explored[edge] == False:
				explored[edge] = True
				stack.append(edge)

	while len(backtrack) > 0:
		order[backtrack.pop()] = t
		t+=1	

def DFS2(G, s):
	
	stack = []
	backtrack = []
	explored[s] = True
	stack.append(s)

	while len(stack) > 0:
		val = stack.pop()
		backtrack.append(val)	
		
		for edge in G[val]:
			if explored[edge] == False:
				explored[edge] = True
				stack.append(edge)
	
	size.append(len(backtrack))

def sort_dict_by_vals(dictionary):
	return sorted(dictionary, key=dictionary.__getitem__)

if __name__ == "__main__":	
	
	N = 600000 #number of nodes
	#N = 9
	graph = defaultdict(list)
	rev = defaultdict(list)

	t = 1 #num of nodes processed so far in 1st pass, gives topological time for each vertex

	#build graph
	for line in open('4.txt'):
		vertex = line.strip().split()
		vertex = map(int, vertex) #map function-useful to convert list of str to ints
		graph[vertex[0]] += vertex[1:]

	#transpose graph

	for k, v in graph.iteritems():
		for elem in v:
			rev[elem] += [k]

	explored = np.zeros(N+1, dtype = bool)

	order = {}

	size = []
	

	#2nd step run DFS-loop on G reversed
	for i in xrange(N, 0, -1):	
		if explored[i] == False:
			DFS(rev,i)

	# 3rd step run DFS-loop on G, has to go through the nodes of the G in a particular order
	# given by the first pass, that is finishing times given by t

	explored = np.zeros(N+1, dtype = bool)
	ordering = sort_dict_by_vals(order)

	while len(ordering)>0:
		i = ordering.pop()
		
		if explored[i] == False:
			DFS2(graph,i)
	
	print sorted(size, reverse = True)
	print("---execution time: %s seconds ---" % (time.time() - start_time))

