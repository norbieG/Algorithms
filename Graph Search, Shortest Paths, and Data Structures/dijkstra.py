from collections import defaultdict
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

	S = []
	dist = {}
	S.append(beg)
	dist[beg] = 0

	while (beg != end):
		max_value = float('inf')
		next_node = 0
		for node in S:
			cost = dist[node]
			for k, v in graph[node].items():
				if k not in S:
					if v + cost < max_value:
						max_value = v + cost
						next_node = k
					
		cost += max_value - cost
		beg = next_node
		S.append(beg)
		dist[beg] = cost
		
	return dist[end]

if __name__ == "__main__":

	data = open('dijkstraData.txt')
	G = read_graph(data)
	source = 1
	#target = 7
	targets = [7,37,59,82,99,115,133,165,188,197]
	results = []
	for target in targets:	
		cost = Dijkstra(G,source, target)
		results.append(cost)
	print results
	print("---execution time: %s seconds ---" % (time.time() - start_time))
	