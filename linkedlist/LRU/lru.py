class Node:
    """Doubly Linked List Node"""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # HashMap to store key -> Node
        self.head = Node(0, 0)  # Dummy head node
        self.tail = Node(0, 0)  # Dummy tail node
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def _remove(self, node: Node):
        """Remove a node from the doubly linked list."""
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add(self, node: Node):
        """Add a node right after the head (most recently used)."""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)  # Move to the front
            self._add(node)
            return node.value
        return -1  # Key not found

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update the value and move to the front
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._add(node)
        else:
            # Insert a new node
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add(new_node)
            self.size += 1

            # If over capacity, remove the least recently used node
            if self.size > self.capacity:
                lru_node = self.tail.prev
                self._remove(lru_node)
                del self.cache[lru_node.key]
                self.size -= 1

# Testing
cache = LRUCache(2)
cache.put(1, 1)  # Cache: {1:1}
cache.put(2, 2)  # Cache: {1:1, 2:2}
print(cache.get(1))  # Output: 1
cache.put(3, 3)  # LRU (2) evicted, Cache: {1:1, 3:3}
