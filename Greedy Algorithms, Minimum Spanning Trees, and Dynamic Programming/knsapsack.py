import numpy as np 


def reconstruct(array, items):
	
	vertices = []

	i = NO_ITEMS 
	j = CAPACITY 

	while i >= 1:

		if array[i-1,j] >= A[i,j]:
			i -=  1
			
		else:
			vertices.insert(0, i)
			j -= items[i][0]
			i -= 1

	print vertices

def read_data():

	items = {}
	file = open('task1.txt')

	for i, line in enumerate(file):
		if i >= 1:
			line = [int(number) for number in line.strip().split()]
			items[i] = (line[1] / 367,line[0]) #tuples (weight, value)
		else:
			line = [int(number) for number in line.strip().split()]
			
			knapsack_size = line[0]
			number_of_items = line[1]

	
	return items, knapsack_size, number_of_items

if __name__ == "__main__":

	items, CAPACITY, NO_ITEMS = read_data()
	# CAPACITY /= 367
	# print CAPACITY
	A = np.zeros((NO_ITEMS+1, CAPACITY+1))


	for i in xrange(1, NO_ITEMS+1):
		for w in xrange(CAPACITY+1):
			
			if w < items[i][0]: 
				A[i,w] = A[i-1,w]

			else:
				A[i,w] = max(A[i-1,w], A[[i-1],w-items[i][0]] + items[i][1])

	
	print A[NO_ITEMS,CAPACITY]
	print A
	reconstruct(A, items)

	# answer 2493893