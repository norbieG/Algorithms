import numpy as np 

probs = [0,.05,.4,.08,.04,.1,.1,.23]

A = np.zeros((len(probs), len(probs)))

for i in xrange(0,len(probs)-1):
	A[i,i+1] = probs[i+1]

for l in xrange(3, len(probs)+1):
	for i in xrange(0, len(probs) - l +1):
		j = i+l-1
		weights = []
		for k in xrange(i+1, j+1):
			weights.append(A[i,k-1] + A[k,j])
		A[i,j] = sum(probs[i+1:j+1]) + min(weights)
			
print A 