# Implementaion of heap data structure for tuples

class Min_Heap: 

	def __init__(self):
		self.heap = [(0,0)]
		self.size = 0
	
	def parent(self, index):
			return self.heap[index/2][0]

	def lchild(self, index):
		return self.heap[2*index]

	def rchild(self, index):
		return self.heap[(2*index)+1]

	def insert(self, item):
	
		
		self.heap.append(item)
		self.size +=1
		self.heapify_up(self.size)

	def heapify_up(self, index):
		
		while index / 2 > 0 and self.heap[index][0] < self.parent(index):
			self.heap[index], self.heap[index/2] = self.heap[index/2], self.heap[index]
			index = index / 2
		

	def extract_min(self):
		
		min_val = self.heap[1]
		self.heap[1], self.heap[self.size] = self.heap[self.size], self.heap[1]
		min_val = self.heap.pop()
		self.size -= 1
		self.heapify_down(1)
		
		return min_val

	def extract_max(self):
		
		max_val = max(self.heap)
		self.heap.remove(max_val)
		self.size -= 1
		return max_val

	def heapify_down(self,i):
		j = float('inf')
		if 2*i > self.size:
			return 0

		elif 2*i < self.size:
			left = 2*i
			right = 2*i + 1

			if self.heap[left][0] < self.heap[right][0]:
				j = left
			else:
				j = right
			
		elif 2*i == self.size:
			j = 2*i
		
		if self.heap[i][0] > self.heap[j][0]:
			self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
			self.heapify_down(j)



class Max_Heap:

	def __init__(self):
		self.heap = [float('inf')]
		self.size = 0
	
	def parent(self, index):
		return self.heap[index/2]

	def lchild(self, index):
		return self.heap[2*index]

	def rchild(self, index):
		return self.heap[(2*index)+1]

	def insert(self, item):
		
		self.heap.append(item)
		self.size +=1 
	
		self.heapify_up(self.size)

	def heapify_up(self, index):
		while index / 2 > 0 and self.heap[index] > self.parent(index):
			self.heap[index], self.heap[index/2] = self.heap[index/2], self.heap[index]
			index = index / 2
		

	def extract_max(self):
		max_val = self.heap[1]
		self.heap[1], self.heap[self.size] = self.heap[self.size], self.heap[1]
		max_val = self.heap.pop()
		self.size -= 1
		self.heapify_down(1)

		return max_val

	

	def heapify_down(self,i):
		j = 1
		if 2*i > self.size:
			return 0

		elif 2*i < self.size:
			left = 2*i
			right = 2*i + 1

			if self.heap[left] > self.heap[right]:
				j = left
			else:
				j = right
			
		elif 2*i == self.size:
			j = 2*i
		
		if self.heap[i] < self.heap[j]:
			self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
			self.heapify_down(j)

	

