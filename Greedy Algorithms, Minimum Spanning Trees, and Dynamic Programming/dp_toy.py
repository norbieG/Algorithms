

def reconstruct(array, G):
	
	vertices = []

	i = len(array)-1

	while i >= 1:

		if array[i-1] >= array[i-2] + G[i-1]:
			i -=  1
			
		else:
			vertices.insert(0, i-1)
			i -= 2

	return vertices


# value of i is the solution to each subproblem

G = [1,4,5,4]

A = [0 for i in xrange(len(G)+1)]

A[1] = G[0]

for i in xrange(2, len(A)):
	A[i] = max(A[i-1], A[i-2]+G[i-1])

# backtrack
print reconstruct(A, G)
