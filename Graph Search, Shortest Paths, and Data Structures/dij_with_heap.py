from collections import defaultdict
from heap import *
import time
start_time = time.time()
#creates graph as dictionary of dictionaries
def read_graph(data):

	graph = defaultdict(dict)
	
	for line in data:
		vals = defaultdict(int)
		line = line.strip().split()
		for nodes in line[1:]:
			nodes = map(int, nodes.split(','))
			assert nodes[1] >= 0
			vals[nodes[0]] = nodes[1]
		graph[int(line[0])] = vals
	
	return graph

#computes the cost of the shortest path
def Dijkstra(graph, beg, end):
	explored = set()
	explored.add(beg)
	S = Min_Heap()
	S.insert({beg: 0})
	nodes = {}


	while (beg != end):
	
		max_value = float('inf')
		next_node = 0
		parent = 0
		for node in S.heap[1:]:
			cost = node.values()[0]
			for k, v in graph[node.keys()[0]].items():
				if k not in explored:
					if v + cost < max_value:
						max_value = v + cost
						next_node = k
						parent = node.keys()[0]
						
		cost += max_value - cost
		explored.add(next_node)
	
		S.insert({next_node : cost})
	
		
	
		beg = next_node
		
	return S.extract_max().values()[0]

if __name__ == "__main__":

	data = open('dijkstraData.txt')
	G = read_graph(data)

	
	source = 1
	
	targets = [7,37,59,82,99,115,133,165,188,197]
	results = []
	for target in targets:	

		cost = Dijkstra(G,source, target)
		results.append(cost)
	print results
	print("---execution time: %s seconds ---" % (time.time() - start_time))
	# [2599, 2610, 2947, 2052, 2367, 2399, 2029, 2442, 2505, 3068]
	