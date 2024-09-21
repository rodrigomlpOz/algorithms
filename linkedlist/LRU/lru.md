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
   
Using a **Doubly Linked List** in combination with a **HashMap** (dictionary) for implementing an **LRU Cache** has several key advantages:

### 1. **Efficient Access to Cache Elements**:
   - **HashMap** provides O(1) time complexity for accessing elements by key. However, a HashMap alone does not maintain the order of elements (especially the most and least recently used).
   - The **Doubly Linked List** is used to maintain the order of usage. The most recently used elements are kept at the **head** of the list, and the least recently used elements are at the **tail**. 
   - By combining both, you get efficient access to elements and the ability to maintain their usage order, both in constant time.

### 2. **Fast Removal and Insertion of Nodes**:
   - A **Doubly Linked List** allows O(1) time complexity for removing or inserting nodes at both the head (most recently used) and the tail (least recently used). 
   - When a cache exceeds its capacity, the least recently used element (the tail) needs to be removed. In a doubly linked list, this can be done in constant time by adjusting the pointers of the adjacent nodes, unlike a singly linked list where removal from the middle or end takes O(n) time.
   
### 3. **Efficient Reordering of Elements**:
   - When a cache element is accessed via a `get` operation, it becomes the most recently used, and we need to move it to the head of the linked list. 
   - With a **Doubly Linked List**, once you find the node (via the HashMap), you can easily remove it from its current position and insert it at the head in constant time O(1), because both forward and backward pointers of the node can be updated efficiently.
   - In a **Singly Linked List**, you'd need to traverse the list to find the previous node to update the pointers, making it less efficient for this purpose.

### 4. **Maintaining Usage Order**:
   - The linked list maintains the order of usage — from the least recently used (tail) to the most recently used (head). 
   - **get()** operations move accessed elements to the head, and **put()** operations insert new elements at the head.
   - The **tail** of the linked list always holds the least recently used element, which can be efficiently removed when the cache exceeds capacity.

### Example Walkthrough:
Consider the following operations for an LRU cache with capacity 2:
   
1. **put(1, 1)**:
   - Insert (1, 1) into the cache. Add a new node with key `1` and value `1` to the **head** of the linked list and store a reference in the HashMap.
   
   **State**:
   ```
   Linked List: 1 <-> None
   HashMap: {1: Node(1,1)}
   ```

2. **put(2, 2)**:
   - Insert (2, 2) into the cache. Add a new node with key `2` and value `2` to the **head** of the linked list and store a reference in the HashMap.
   
   **State**:
   ```
   Linked List: 2 <-> 1 <-> None
   HashMap: {1: Node(1,1), 2: Node(2,2)}
   ```

3. **get(1)**:
   - Access key `1`. Move the corresponding node to the **head** of the list (it becomes the most recently used).
   
   **State**:
   ```
   Linked List: 1 <-> 2 <-> None
   HashMap: {1: Node(1,1), 2: Node(2,2)}
   ```

4. **put(3, 3)**:
   - Cache is full (capacity is 2). Insert key `3` and value `3`. To make room, remove the **tail** node (key `2`), which is the least recently used. Insert a new node with key `3` at the **head** of the list.
   
   **State**:
   ```
   Linked List: 3 <-> 1 <-> None
   HashMap: {1: Node(1,1), 3: Node(3,3)}
   ```

5. **get(2)**:
   - Key `2` is not in the cache, so return `-1`.

### Advantages of Combining HashMap and Doubly Linked List:
1. **O(1) Time Complexity** for both `get` and `put` operations.
2. **Constant-Time Deletion and Insertion** at the head or tail of the list using the doubly linked list.
3. **Efficient Reordering** of recently accessed elements by moving nodes to the head of the list.
4. **Space Efficiency**: The use of a doubly linked list and hashmap ensures that only the necessary nodes are stored and efficiently managed without wasted space.

By leveraging both a **HashMap** for quick access and a **Doubly Linked List** for maintaining order and efficient removal/insertion, you ensure an optimal LRU Cache solution.

