class Node:
	def __init__(self, value):
		self.value = value
		self.prev = None


class Queue:
	def __init__(self):
		self.head = None
		# self.tail = None
		self.count = 0

	def last_item(self):
		last = self.head
		while last.prev is not None:
			last = last.prev
		return last.value

	def peek(self):
		if self.head is None:
			raise ValueError("Queue is empty")
		return self.head.value

	def pop(self):
		item = self.peek()
		self.head = self.head.prev
		self.count -= 1
		return item

	def __len__(self):
		return self.count

	def __contains__(self, value):
		last = self.head
		while last.prev is not None:
			if last.value == value:
				return True
			last = last.prev
		return False


	def add(self, value):
		if self.head is None:
			new_node = Node(value)
			self.head = new_node
			self.count += 1
			return
		last = self.head
		while last.prev is not None:
			last = last.prev
		new_node = Node(value)
		last.prev = new_node
		self.count += 1

	def is_empty(self):
		return self.count == 0

	def __repr__(self):
		if self.head is None:
			return "[]"
		all_nodes = []
		last = self.head
		while last.prev is not None:
			all_nodes.append(last.value)
			last = last.prev
		all_nodes.append(last.value)
		return f"{all_nodes}"

	def clear(self):
		self.head = None


if __name__=="__main__":
	queue = Queue()
	print(queue)
	print(f"Is Empty: {queue.is_empty()}")

	queue.add(1)
	queue.add(2)
	queue.add(3)
	queue.add(4)
	queue.add(5)
	print(queue)
	print(queue.is_empty())
	print(f"Length: {len(queue)}")

	print("--------")
	print(queue.last_item())
	print(queue.peek())
	print(queue.pop())
	print(queue.pop())
	print(queue.pop())
	print(queue)
	print(queue.pop())

	print(queue)
	print(queue.is_empty())
	print(len(queue))
	print(queue.pop())

