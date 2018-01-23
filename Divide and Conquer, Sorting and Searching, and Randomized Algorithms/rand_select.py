# randomised selection algorithm
# takes as input array, its length n and statistics s
# running time O(n)
# output: a number given statistics, i.e. if statistics 3 , output 3rd smallest int

import random
import os
def Rselect(A,n,s):

	assert len (A)>=s and s>0, 'to high/low statistics'

	if len(A) == 1:
		print 'result',A[0]

	else:
		p = random.randrange(0,n)
		partition (A,p,n,s)

def partition (A, p, n, s):
	
	pivot = A[p]
	A[0], A[p] = A[p], A[0]
	l = 0
	i = l +1
	
	for j in xrange (l+1, n):
	
		if A[j] < pivot: #is newly seen element less then pivot
			A[j],A[i] = A[i],A[j]
			i += 1 #increment the boundry between the elements smaller and biggger than the pivot
	A[l],A[i-1] = A[i-1],A[l]
	
	j = i-1
	if j == s-1:
		print 'result',A[j]
		 
	elif j>s-1:
		return Rselect(A[:j],j ,s)
	
	else:
		return Rselect(A[j+1:],n-j-1 ,s-j-1)
	
A = [1,4,2,5,0,6]
# for i,line in enumerate(open(os.path.abspath("q2.txt"))):
# 	A.append(int(line.strip()))

#random.seed(1)

Rselect(A, len(A), 2)
