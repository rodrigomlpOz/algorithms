### Problem Statement: 
Design and implement a data structure for Least Recently Used (LRU) Cache. It should support the following operations: `get(key)` and `put(key, value)`.

1. **get(key)** - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
2. **put(key, value)** - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least recently used item before inserting a new item.

The cache should be initialized with a positive capacity.

### Function Definition:
```python
class LRUCache:

    def __init__(self, capacity: int):
        # Initialize the cache with a given capacity
        pass

    def get(self, key: int) -> int:
        # Return the value if the key exists, otherwise return -1
        pass

    def put(self, key: int, value: int) -> None:
        # Insert the key-value pair into the cache
        pass
```

### Example Usage:
```python
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
```

### High-Level Solution:

- **Data Structures:**
  ### High-Level Solution using **HashMap (Dictionary)** and **Doubly Linked List**:

#### 1. **Data Structures**:
- **HashMap (Dictionary)**: 
  - Maps the `key` to a node in the doubly linked list. This allows for O(1) access to the cache elements.
  
- **Doubly Linked List**: 
  - Maintains the order of elements based on usage. 
  - The **head** of the list will always contain the most recently used (MRU) element, while the **tail** will contain the least recently used (LRU) element.
  - Each node will store the key and value, and will have pointers to the previous and next nodes to allow fast removal or reordering of nodes.
  
#### 2. **Operations**:
- **get(key)**:
  - If the `key` is found in the HashMap, retrieve the corresponding node from the doubly linked list.
  - Move that node to the front (head) of the list, marking it as the most recently used.
  - Return the value of the node.
  - If the key is not found, return `-1`.
  
- **put(key, value)**:
  - If the `key` already exists, update its value and move the corresponding node to the front of the list.
  - If the `key` does not exist:
    - Create a new node with the `key` and `value`.
    - Insert the new node at the front of the list.
    - Add the `key` and node to the HashMap.
  - If adding the new node causes the cache to exceed its capacity, remove the node at the tail (LRU node) and remove its key from the HashMap.

#### 3. **Edge Case**:
- If the cache is empty, handle the first insertion.
- When the cache reaches its capacity, remove the least recently used item (from the tail).

### High-Level Flow:
1. **Initialization**:
   - A `HashMap` to map keys to their corresponding nodes in the linked list.
   - A `Doubly Linked List` to store the order of elements based on access.
   
2. **get(key)**:
   - Look up the node in the HashMap.
   - If it exists, move the node to the head of the list (as it is now the most recently used).
   - Return the node's value.
   - If it doesn't exist, return `-1`.
   
3. **put(key, value)**:
   - If the key already exists, update the node's value and move it to the head of the list.
   - If the key is new, create a node, add it to the head of the list, and insert it into the HashMap.
   - If the cache size exceeds the capacity, remove the node at the tail (least recently used) and remove its key from the HashMap.

#### Time Complexity:
- **get(key)**: O(1) for both the hashmap lookup and moving a node in the linked list.
- **put(key, value)**: O(1) for inserting or removing nodes from the linked list and updating the hashmap.

#### Example:

```plaintext
Capacity: 2

put(1, 1) --> Cache: {1:1}
put(2, 2) --> Cache: {1:1, 2:2}
get(1)    --> Returns 1, Cache: {2:2, 1:1} (1 is most recently used now)
put(3, 3) --> Cache: {1:1, 3:3} (2 is least recently used, so it is removed)
get(2)    --> Returns -1 (2 was removed)
put(4, 4) --> Cache: {3:3, 4:4} (1 is removed as it is least recently used)
get(1)    --> Returns -1 (1 was removed)
get(3)    --> Returns 3, Cache: {4:4, 3:3}
get(4)    --> Returns 4, Cache: {3:3, 4:4}
```

This solution ensures that both **get** and **put** operations run in constant time O(1) by leveraging the combination of a hashmap and doubly linked list.

- **Operations:**
  - For `get(key)`:
    - If the key exists, move it to the end of the ordered dictionary and return its value.
    - If the key doesn't exist, return -1.
  - For `put(key, value)`:
    - If the key already exists, update its value and move it to the end of the ordered dictionary.
    - If the key doesn't exist, insert it. If the cache exceeds capacity, remove the first (least recently used) key-value pair from the ordered dictionary.

