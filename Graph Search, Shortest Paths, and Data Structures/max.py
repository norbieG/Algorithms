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
		print 'index', index
		print self.parent(index)
		# print self.heap[index] < self.parent(index)
		while index / 2 > 0 and self.heap[index] < self.parent(index):
			self.heap[index], self.heap[index/2] = self.heap[index/2], self.heap[index]
			index = index / 2
		

	def extract_max(self):
		max_val = self.heap[1]
		self.heap[1], self.heap[self.size] = self.heap[self.size], self.heap[1]
		max_val = self.heap.pop()
		self.size -= 1
		self.heapify_up(1)

		return max_val

	# def extract_max(self):
		
	# 	max_val = max(self.heap)
	# 	self.heap.remove(max_val)
	# 	self.size -= 1
	# 	return max_val

	def heapify_up(self,i):
		j = float('inf')
		if 2*i > self.size:
			return 0

		elif 2*i > self.size:
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
			self.heapify_up(j)
