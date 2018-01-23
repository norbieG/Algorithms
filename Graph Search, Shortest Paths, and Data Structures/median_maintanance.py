#create Heap low and heap high
#if we split 20 numbers between two heaps, the highest in Hlow will be the tenth element and 
# the lowest in H high will be the 11th. when the 21st element comes,
# if it is smaller the the HL max, it goes to HL otherwise if is biiger then HHmin go to HH
# if between put anywhere is a median.
# you may not have 50/50 split in the numbers if everything happens to go to one H, then:
# to keep balance extract max from HL and add to HH or the other way around
# 2nd POINT: how to compute the median? either the max of HL and /or min of HH. depends if i is even or odd.
# if it is even both are medians if odd then whichever heap has more elements than the other one

from heap import *

HL = Max_Heap() 
HH = Min_Heap()

result = 0

i = 0
for number in open('median.txt'):
	i+=1
	d = int(number.strip())
	
	if HL.size > 0 and HH.size > 0: 
	
		if d < HL.heap[1]:
			HL.insert(d)
		elif d > HH.heap[1]:
			HH.insert(d)
		else:
			HH.insert(d)

	elif HL.size <= 1: 
		
		HL.insert(d)
			
	else:
		HH.insert(d)


	if HH.size - HL.size > 1:
		min_HH = HH.extract_min()

		HL.insert(min_HH)

	elif HL.size - HH.size > 1:
		max_HL = HL.extract_max()
		
		HH.insert(max_HL)


	if i % 2 != 0:
		if HL.size<HH.size:
			result += HH.heap[1]
		else:
			result += HL.heap[1]
		
	else:
		result += HL.heap[1]
		
print result % 10000
