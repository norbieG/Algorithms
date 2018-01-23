from collections import defaultdict
import operator
import random
from heap import *



def read_graph(data): #undirected graph read in both ways
	vertices = set()
	graph = defaultdict(list)
	
	for i, line in enumerate(data):

		if i > 0:
			
			vals = defaultdict(int)
			line = [float(e) for e in line.split()]
			
			graph[float(line[0])].append((line[1],line[2]))
			graph[float(line[1])].append((line[0],line[2]))
			vertices.add(line[0])
			vertices.add(line[1])
	return graph, vertices



if __name__ == "__main__":

	data = open('city.txt')
	G, V = read_graph(data)
	seed = 1
	X = set()
	X.add(seed)
	T = []
	val = 0
	while X!=V:
	# for i in xrange(7):
		max_value = float('inf')
		next_node = 0 
		previous = 0
		for node in X:
			for edge in G[node]:
				if edge[0] not in X:
					if edge[1] < max_value:
						max_value = edge[1]
						next_node = edge[0]
						previous = node
		val+=max_value
		T.append((previous, next_node))
		X.add(next_node)
		

	print 'spannig tree is:', T
	print 'min cost: ', val


	
