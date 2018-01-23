import time
from collections import defaultdict

start_time = time.time()

data = []

def binary_search(A,p,r,x):
	if p > r:
		return r
	else:
		q= (p+r)/2	
		if x == A[q]:
			return q
		elif x < A[q]:
			return binary_search(A,p,q-1,x)
		else:
			return binary_search(A,q+1,r,x)


for line in open('sum.txt'):
	line = line.strip().split()
	for digit in line:
		data.append(int(digit))

data = sorted(data)

print("---execution time: %s seconds ---" % (time.time() - start_time))

results = set()
counter = 0
start_time1 = time.time()
for digit in data:

	
	
	left = binary_search(data,0,len(data)-1,-20000 - digit)
	right = binary_search(data,0,len(data)-1,20000 - digit)

	for o in  data[left:right+1]:
		if digit+o >= -10000 and digit+o<=10000:
			results.add(digit+o)

print("---execution time: %s seconds ---" % (time.time() - start_time1))

print len(results)



	


