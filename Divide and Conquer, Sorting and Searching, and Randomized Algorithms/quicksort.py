#quicksort with median of three partition method

import os
import numpy as np

def quicksort (A,l,r,p):
	
	if l < r:

		i,comparisons = partition (A, l, r)
		quicksort(A, l, i - 1,p)	
		quicksort(A, i + 1, r,p)
		p.append(comparisons)

def partition (A, l, r):
	counter = 0
	median = sorted([A[l],find_middle(A[l:r+1]), A[r]])[1] #find median
	index_med = A.index(median)
	i = l + 1
	A[l], A[index_med] = A[index_med],A[l] #swap positions
	
	pivot = A[l]
	
	counter += len(A[l+1:r+1])
	
	for j in xrange (l+1, r+1):
		if A[j] < pivot: #is newly seen element less then pivot
			A[j],A[i] = A[i],A[j]
			i += 1 #increment the boundry between the elements smaller and biggger than the pivot
	A[l],A[i-1] = A[i-1],A[l]
	i-=1
	return i,counter

def find_middle(A):
	if len(A) % 2 == 0:
		return  A[(len(A)/2)-1]
	else:
		return A[(len(A)/2)] 



# A = [9,8,2,5,4,7,6,1]
p = []

A = []
for i,line in enumerate(open(os.path.abspath("q2.txt"))):
	A.append(int(line.strip()))
quicksort(A, 0, len(A) - 1,p)
print sum(p)
print A
#answer a: 162085
#answer b: 164123
#answer c: 138382
