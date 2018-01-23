import random
from collections import defaultdict
SIZE = 5

class Hash():

	

	def __init__(self, filename):
		self.keys = self.read_from_filename(filename)
		self.hash_table = [[] for i in xrange(SIZE)]

	def read_from_filename(self,file):

		elements = set()

		try:

			for line in open(file):
				line = line.strip().split()
				for digit in line:
					elements.add(int(digit))

		except IOError:
			print "I/O error, please ensure your filename was correct"

		return elements
	
	def insert(self):
		pass

	def delete(self):
		pass

	def look_up(self):
		pass

	

# hash_function = defaultdict(int)
