class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def remove(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                self.table[index].remove(pair)
                return

# Create a hash table with a size of 10
hash_table = HashTable(10)

# Insert key-value pairs into the hash table
hash_table.insert("apple", 5)
hash_table.insert("banana", 8)
hash_table.insert("cherry", 3)

# Retrieve values by keys
apple_value = hash_table.get("apple")
banana_value = hash_table.get("banana")
cherry_value = hash_table.get("cherry")
nonexistent_value = hash_table.get("grape")

print("Value of 'apple':", apple_value)
print("Value of 'banana':", banana_value)
print("Value of 'cherry':", cherry_value)
print("Value of 'grape':", nonexistent_value)

# Remove a key-value pair from the hash table
hash_table.remove("banana")

# Attempt to retrieve the value of the removed key
removed_value = hash_table.get("banana")

print("Value of 'banana' after removal:", removed_value)
