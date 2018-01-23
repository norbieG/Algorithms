# linked list and node classes


class Node:

	def __init__ (self, init_data):
		self.root = init_data
		self.parent = init_data


class Linked_list:

	def __init__ (self):
		self.head = None #self.head points at the last node added to the list
		self.tail = None


	def add(self, item):
		temp = Node(item)
		temp.set_next(self.head)
		self.head = temp
		self.set_tail()

	def swap_heads(self, new_head):
		current = self.head
	
		while current != None:
			

			current = current.get_next()


	def traverse(self):
		current = self.head
		print current.get_data()
		tail = self.tail
		while current != None:
			print 'current node', current.get_data(), 'tail', self.tail.get_data(), 'head', self.head.get_data()

			current = current.get_next()


	def set_tail(self):
		current = self.head
		while current != None:
			self.tail = current
			current = current.get_next()

		


		
			
			
		















# 