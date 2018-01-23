from heap import *
from union_find import *



def read_graph(data): #undirected graph read in both ways
	
	
	H = Min_Heap()
	for i, line in enumerate(data):
		if i > 0:
			line = [int(e) for e in line.split()]
			edge = (line[2],line[0],line[1])
			H.insert(edge)
	return H

if __name__ == "__main__":

	data = open('cluster1.txt')
	first_line = data.readline()
	subsets = int(first_line.strip())
	H = read_graph(data)
	forest = []	
	tree = Union_Find(subsets + 1)

	while len(H.heap) > 1:
		cheapest = H.extract_min()
		if tree.find(cheapest[1]) != tree.find(cheapest[2]):	
			tree.union(cheapest[1], cheapest[2])
			forest.append(cheapest)

	print forest



# answer 106




