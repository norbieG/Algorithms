#sets up a work queue, each job has a weight and a lenght, priorioty gets a job with a larger l/w ratio or difference.
#merge sort sorts the jobs by the priority, ties are sorted by choosing a job with higher weight.

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
	
	for k in xrange(p, r+1):
		if first_half[i][0] >= second_half[j][0]:
			
			A[k] = first_half[i]
			i+=1
			if i == len(first_half):
				A[k+1:r+1] = second_half[j:]
				
				return A			
		else:

			if first_half[i][0] < second_half[j][0]:

				A[k] = second_half[j]
		    	j+=1
		    	if j == len(second_half):
		    		A[k+1:r+1] = first_half[i:]
		    		
		    		return A

data = open('jobs.txt')

first_line = data.readline()
first_line = int(first_line.strip())

job_list = [0 for i in  xrange(first_line)]


for row, line in enumerate(data):
	pair = map(int,line.strip().split())

	job_list[row] = (pair[0] -(pair[1]), pair[0],pair[1]) #ratio / difference



merge_sort(job_list, 0, len(job_list)-1)

for i in xrange(0,len(job_list)):
    for j in xrange(i, len(job_list)):
        if job_list[i][0] == job_list[j][0]:
            if job_list[i][1] < job_list[j][1]:
                job_list[i],job_list[j] = job_list[j],job_list[i]
        else:
        	break

score = 0 
C = 0 #keep track of length
for i in xrange(0,len(job_list)):
	C += job_list[i][2]
	score +=job_list[i][1] * C
	
print score
