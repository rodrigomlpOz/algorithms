### Problem Statement:
Design a data structure, `QueueMax`, that supports the following operations efficiently:

1. **enqueue(x)**: Add an element `x` to the back of the queue.
2. **dequeue()**: Remove an element from the front of the queue.
3. **max()**: Retrieve the maximum element currently in the queue.

All of these operations should be done in **constant time**.

### Function Signature:
```python
class QueueMax:
    def enqueue(self, x):
        pass
    
    def dequeue(self):
        pass
    
    def max(self):
        pass
```

### Function Calls Example:
```python
q = QueueMax()

# Enqueue operations
q.enqueue(1)
q.enqueue(3)
q.enqueue(2)
print(q.max())  # Output: 3 (max in [1, 3, 2])

q.dequeue()
print(q.max())  # Output: 3 (max in [3, 2])

q.dequeue()
print(q.max())  # Output: 2 (max in [2])
```

### High-Level Solution:

1. **Data Structure Choice**:
   - We'll use two deques (`queue` and `max_queue`):
     - `queue`: The regular queue for handling `enqueue` and `dequeue` operations.
     - `max_queue`: A specialized deque to maintain elements in decreasing order for constant-time maximum retrieval.
  
2. **enqueue(x)**:
   - Add the element `x` to the back of `queue`.
   - While the last element of `max_queue` is smaller than `x`, pop elements from the back of `max_queue`. Then, add `x` to the back of `max_queue`. This ensures `max_queue` maintains the maximum element at the front.
  
3. **dequeue()**:
   - Remove the front element from `queue`. 
   - If the element being removed is also the front of `max_queue`, remove it from `max_queue` as well. This keeps the `max_queue` updated as elements are removed.
  
4. **max()**:
   - Return the front element of `max_queue`, which is always the maximum element in the queue.


### Time Complexity:
- **enqueue(x)**: O(1) amortized time, as elements are added to the queue and `max_queue` is maintained with only necessary pops to ensure the correct maximum.
- **dequeue()**: O(1) time, as elements are simply removed from the front.
- **max()**: O(1) time, as the maximum value is always stored at the front of `max_queue`.

### Space Complexity:
- **O(n)**, where `n` is the number of elements in the queue, since both `queue` and `max_queue` store at most `n` elements.

This solution efficiently handles all three operations in constant time, ensuring that the maximum element in the queue is always available without needing to scan through the queue.
