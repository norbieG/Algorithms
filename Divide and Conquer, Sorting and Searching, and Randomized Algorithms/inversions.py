import os
import numpy as np

#merge sort input is a list A and indices for begining and end
#count amount of inversions to sort the list

def merge_sort(A, p, r, counter ):

	if p >= r:	
		pass

	elif p < r:

		q = (p + r) / 2
		
		merge_sort(A, p, q,counter)
		merge_sort(A, q+1, r,counter)
		merge(A,p,q,r,counter)

def merge(A, p, q, r,counter):

	i,j = 0,0 
	first_half = A[p:q+1]	
	second_half = A[q+1:r+1]
	
	for k in range(p, r+1):
		if first_half[i] <= second_half[j]:
			A[k] = first_half[i]
			i+=1
			if i == len(first_half):
				A[k+1:r+1] = second_half[j:]
				
				return A			
		else:

			if first_half[i] > second_half[j]:

				A[k] = second_half[j]
		    	j+=1
		    	
		    	counter.append(len(first_half[i:]))
 	
		    	if j == len(second_half):
		    		A[k+1:r+1] = first_half[i:]
		    		
		    		return A
		

A = [10,9,8,7,6,5,4,3,2,1]
#2407905288
#A = np.zeros(100000, int)
counter = []
#for i,line in enumerate(open(os.path.abspath("IntegerArray.txt"))):	
#	A[i] = (int(line.strip()))

#print len(A)
A = np.array(A)
#print A
merge_sort(A, 0, len(A)-1, counter)

print '# of inversions is: ', sum(np.array(counter))
#print A

