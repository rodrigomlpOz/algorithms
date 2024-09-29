class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # This will hold the keys and Node references
        self.head = Node(0, 0)  # Dummy head of the doubly linked list
        self.tail = Node(0, 0)  # Dummy tail of the doubly linked list
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):
        """Removes a node from the doubly linked list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add(self, node: Node):
        """Adds a node right after the head of the doubly linked list."""
        next_node = self.head.next
        node.next = next_node
        node.prev = self.head
        self.head.next = node
        next_node.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)  # Remove the node from its current position
            self._add(node)  # Move it to the front (mark as recently used)
            return node.value
        return -1

    def put(self, key: int, value: int):
        # If the key is already in the cache, update the node and move it to the front
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._add(node)
        else:
            # If the cache is full, evict the least recently used node
            if len(self.cache) >= self.capacity:
                lru_node = self.tail.prev
                self._remove(lru_node)
                del self.cache[lru_node.key]
    
            # Insert the new node at the front of the list
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add(new_node)


# Example usage:
lru_cache = LRUCache(2)
lru_cache.put(1, 1)  # Cache is {1=1}
lru_cache.put(2, 2)  # Cache is {1=1, 2=2}
print(lru_cache.get(1))  # Returns 1, Cache is {2=2, 1=1}
lru_cache.put(3, 3)  # Evicts key 2, Cache is {1=1, 3=3}
print(lru_cache.get(2))  # Returns -1 (not found)
lru_cache.put(4, 4)  # Evicts key 1, Cache is {4=4, 3=3}
print(lru_cache.get(1))  # Returns -1 (not found)
print(lru_cache.get(3))  # Returns 3, Cache is {4=4, 3=3}
print(lru_cache.get(4))  # Returns 4, Cache is {3=3, 4=4}
