
class Union_Find:

	def __init__ (self, N):

		self.parents = [i for i in xrange(N)]
		self.size = [1 for i in xrange(N)]



	def find(self, vertex):

		if vertex != self.parents[vertex]:
			self.parents[vertex] = self.find(self.parents[vertex])

		return self.parents[vertex]



	def union(self, vertex1, vertex2):

		root1 = self.find(vertex1)
		root2 = self.find(vertex2)

		if self.size[root1] > self.size[root2]:
			self.parents[root2] = root1

		else:
			self.parents[root1] = root2

		if self.size[root1] == self.size[root2]:
			self.size[root2] += 1
