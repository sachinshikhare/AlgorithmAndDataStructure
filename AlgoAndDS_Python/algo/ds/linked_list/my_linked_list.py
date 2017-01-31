class Node:
	def __init__(self, data=None, next_node=None):
		self.data = data
		self.next_node = next_node

class LinkedList(object):
	def __init__(self, head=None):
		self.head = Node()
		self.length = 0;
		
	def add_at_end(self, data):
		node = Node(data)
		if self.head == None:
			self.head.next_node = node
		else:
			current_node = self.head
			while current_node.next_node != None:
				current_node = current_node.next_node
			current_node.next_node = node
		self.length+=1
	
	def add_at_start(self, data):
		node = Node(data)
		if self.head == None:
			self.head.next_node = node
		else:
			node.next_node = self.head.next_node
			self.head.next_node = node
		self.length+=1
			
	def remove_first(self):
		if self.length == 0:
			return None
		else: 
			removed_node = self.head.next_node 
			self.head.next_node = self.head.next_node.next_node;
			return removed_node.data
		self.length-=1
		
	def remove_last(self):
		if self.length == 0:
			return None
		elif self.length == 1:
			removed_node = self.head.next_node
			self.head.next_node = None
			return removed_node.data
		else:
			current = self.head.next_node
			while current.next_node.next_node != None:
				current = current.next_node
			removed_node = current.next_node
			current.next_node = None
			return removed_node.data
		self -= 1
		
	def print_linked_list(self):
		if self.length == 0:
			print("")
		else:
			string = ""
			current = self.head.next_node
			string = current.data
			while current.next_node != None:
				current = current.next_node
				string += ", " + current.data
			print(string)