import time
from collections import defaultdict
start_time = time.time()
data = set()
numbers = defaultdict(list)

divisor = 1000


for line in open('sum.txt'):
	line = line.strip().split()
	for digit in line:
		data.add(int(digit))
keys = set()		
for digit in data:
	key = digit/divisor
	keys.add(key)
	numbers[digit/divisor] += [digit]
print len(keys)


print("---execution time: %s seconds ---" % (time.time() - start_time))


counter = 0
for t in xrange(-10000,10001):
	print t
	start_time1 = time.time()
	for x in data:
		y = t-x
		
		key = y/divisor
		
		if y in numbers[key]:
			counter +=1 
			print 'x',x,'t',t,'y',y,'key',key,'avail:', numbers[key]
			break

	print counter
	
	print("---execution time: %s seconds ---" % (time.time() - start_time1))
print counter


#result  427, 5h

	


