class Hashmap:
	def __init__(self, capacity):
		self.capacity = capacity
		self.size = 0
		self.buckets = [[] for _ in range(self.capacity)]

	def _hash_key(self, key):
		str_key = str(key)
		hashed_key = 0
		for char in str_key:
			hashed_key = (hashed_key + ord(char)) % self.capacity
		return hashed_key

	def __contains__(self, key):
		hashed_key = self._hash_key(key)
		bucket = self.buckets[hashed_key]
		for k, v in bucket:
			if k == key:
				return True
		return False

	def put(self, key, value):
		hashed_key = self._hash_key(key)
		bucket = self.buckets[hashed_key]
		for i, (k, v) in enumerate(bucket):
			if k == hashed_key:
				bucket[i] = (key, value)
				break
		else:
			self.size += 1
			bucket.append((key, value))

	def __len__(self):
		return self.size

	def remove(self, key):
		hashed_key = self._hash_key(key)
		bucket = self.buckets[hashed_key]
		for i, (k, v) in enumerate(bucket):
			if key == k:
				self.size -= 1
				del bucket[i]
				break
		else:
			raise KeyError("This Key does not exist!")

	def keys(self):
		return [k for bucket in self.buckets for k, _ in bucket]

	def values(self):
		return [v for bucket in self.buckets for _, v in bucket]

	def items(self):
		return [(k, v) for bucket in self.buckets for k, v in bucket]



if __name__ == "__main__":
	hash_map = Hashmap(32)

	print(len(hash_map))
	print(hash_map.buckets)
	hash_map.put("Job", "Programmer")
	hash_map.put("Age", 30)
	hash_map.put("City", "Moscow")
	hash_map.put("Clever", False)

	print(hash_map.items())
	print(hash_map.keys())
	print(hash_map.values())
	print(hash_map.buckets)
	print(hash_map)

	print("Job" in hash_map)
	hash_map.remove("Job")
	print(hash_map.buckets)


