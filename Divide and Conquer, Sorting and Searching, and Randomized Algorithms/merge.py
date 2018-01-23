#merge sort input is a list A and indices for begining and end

def merge_sort(A, p, r):
        
	
	if p >= r:	
		pass

	elif p < r:

		q = (p + r) / 2
		
		merge_sort(A, p, q)
		merge_sort(A, q+1, r)
		merge(A,p,q,r)
		
def merge(A, p, q, r):
	
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
		    	if j == len(second_half):
		    		A[k+1:r+1] = first_half[i:]
		    		
		    		return A
		

#A = [0,1,3,2,4,5,4,9,7,8,9]
A=[2,1,9,8,7,6,5,4,3,9,8,7,6,23,45,56,0,43242,0,46,75686,5,24545,23,67867886]
merge_sort(A, 0, len(A)-1)
print A

