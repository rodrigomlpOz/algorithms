from collections import defaultdict

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        # Initialize the cache with a given capacity
        self.capacity = capacity
        self.node_dict = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, key: int) -> int:
        # Return the value if the key exists, otherwise return -1
        pass

    def put(self, key: int, value: int) -> None:
        # Insert the key-value pair into the cache
        pass



# Initialize the cache with capacity 2
cache = LRUCache(2)

cache.put(1, 1)      # Cache: {1:1}
cache.put(2, 2)      # Cache: {1:1, 2:2}
print(cache.get(1))  # Returns 1, Cache: {2:2, 1:1}
cache.put(3, 3)      # LRU key 2 is removed, Cache: {1:1, 3:3}
print(cache.get(2))  # Returns -1 (not found)
cache.put(4, 4)      # LRU key 1 is removed, Cache: {3:3, 4:4}
print(cache.get(1))  # Returns -1 (not found)
print(cache.get(3))  # Returns 3, Cache: {4:4, 3:3}
print(cache.get(4))  # Returns 4, Cache: {3:3, 4:4}