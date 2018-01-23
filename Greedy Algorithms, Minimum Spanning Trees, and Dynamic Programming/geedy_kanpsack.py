import numpy as np 
from operator import itemgetter

def read_data():

	items = {}
	file = open('task2.txt')

	for i, line in enumerate(file):
		if i >= 1:
			line = [int(number) for number in line.strip().split()]
			items[i] = (line[0],line[1]) 
		else:
			line = [int(number) for number in line.strip().split()]
			
			knapsack_size = line[0]
			number_of_items = line[1]

	
	return items, knapsack_size, number_of_items

if __name__ == "__main__":

	items, CAPACITY, NO_ITEMS = read_data()
	items_ordered = sorted(items.items(), key=itemgetter(1))
	print items_ordered
	
	result = 0
	weight = 0
	print CAPACITY
	while(weight < CAPACITY):
		elem = items_ordered.pop()
		
		weight +=elem[1][1]
		result+=elem[1][0]
		print 'weight', weight
		print result
	# answer 2493893