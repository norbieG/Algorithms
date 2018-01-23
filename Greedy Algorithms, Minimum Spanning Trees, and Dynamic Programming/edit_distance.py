import numpy as np 

def reconstruct(array):
	
	vertices = []

	i = len(s1)
	j = len(s2)


	while i >= 0:

		if array[i-1,j] < A[i,j] and array[i-1,j] < A[i-1,j-1]:
			vertices.insert(0,(i, j))
			i -=  1

		elif array[i,j-1] < A[i,j] and array[i,j-1] < A[i-1,j-1]:
			vertices.insert(0,(i, j))
			j -=  1

		else:
			vertices.insert(0,(i, j))
			i -= 1
			j -= 1
			
	print vertices


def diff(i,j):

	if s1[i-1] == s2[j-1]:
		return 0
	else:
		return 1


if __name__ == "__main__":

	s1 = 'azced'
	s2 = 'abcdef'


	A = np.zeros((len(s1)+1, len(s2)+1))

	for i in xrange(len(s1)+1):
		A[i,0] = i

	for j in xrange(len(s2)+1):
		A[0,j] = j


	for i in xrange(1, len(s1)+1):
		for j in xrange(1, len(s2)+1):

			A[i,j] = min(diff(i,j) + A[i-1, j-1], 1 + A[i-1, j], 1 + A[i, j-1])


	print A

	reconstruct(A)