### Problem Statement:
Implement a queue using two stacks. The queue should support the following operations:
1. **enqueue(x)**: Add an element `x` to the back of the queue.
2. **dequeue()**: Remove the element from the front of the queue.
3. **peek()**: Get the front element without removing it.
4. **empty()**: Return whether the queue is empty.

The goal is to simulate the behavior of a queue using only two stacks, where a queue follows **FIFO** (First In, First Out) order, and a stack follows **LIFO** (Last In, First Out) order.

### Approach:
We can use two stacks to implement a queue:
1. **Input Stack (stack_in)**: This stack is used to handle the **enqueue** operation.
2. **Output Stack (stack_out)**: This stack is used to handle the **dequeue** and **peek** operations. 

When we need to **dequeue** or **peek**, if the output stack is empty, we move all elements from the input stack to the output stack. This reverses the order of elements, simulating the queue's FIFO behavior.

### Function Signature:
```python
class QueueFromStacks:
    def enqueue(self, x):
        pass
    
    def dequeue(self):
        pass
    
    def peek(self):
        pass
    
    def empty(self):
        pass
```

### High-Level Solution:
1. **enqueue(x)**: Push the element `x` onto the `stack_in`. This is an O(1) operation.
2. **dequeue()**:
   - If `stack_out` is empty, transfer all elements from `stack_in` to `stack_out` to reverse the order.
   - Pop the top element from `stack_out` (the front of the queue). If both stacks are empty, return `None`.
3. **peek()**:
   - If `stack_out` is empty, transfer all elements from `stack_in` to `stack_out`.
   - Return the top element of `stack_out` (the front of the queue).
4. **empty()**: Return whether both `stack_in` and `stack_out` are empty.

### Solution Code:

```python
class QueueFromStacks:
    def __init__(self):
        pass

    def enqueue(self, x):
        # Simply push the element onto the stack_in
        pass

    def dequeue(self):
        # If stack_out is empty, transfer all elements from stack_in to stack_out
        pass

    def peek(self):
        # If stack_out is empty, transfer elements from stack_in to stack_out
        pass

    def empty(self):
        # The queue is empty if both stack_in and stack_out are empty
        pass
```

### Explanation:

1. **Two Stacks**:
   - `stack_in`: This is used to handle the **enqueue** operations. Every element is pushed onto this stack as it arrives.
   - `stack_out`: This is used for the **dequeue** and **peek** operations. When it is empty and a dequeue or peek is requested, we move all elements from `stack_in` to `stack_out`. This reverses the order of elements, making the oldest element available at the top.

2. **Operations**:
   - **enqueue(x)**: Simply push `x` onto `stack_in`. This operation is O(1).
   - **dequeue()**: If `stack_out` is empty, transfer all elements from `stack_in` to `stack_out`, then pop from `stack_out`. This operation is O(n) in the worst case when `stack_out` is empty, but amortized over many operations, it is O(1).
   - **peek()**: Similar to `dequeue()`, if `stack_out` is empty, transfer elements from `stack_in` and return the top element of `stack_out`. This is also O(1) on average.
   - **empty()**: Return True if both `stack_in` and `stack_out` are empty, otherwise return False. This operation is O(1).

### Time Complexity:
- **enqueue(x)**: O(1) time.
- **dequeue()**: Amortized O(1) time. Although the worst-case time is O(n) (when elements are transferred from `stack_in` to `stack_out`), the amortized cost over multiple operations is O(1).
- **peek()**: Amortized O(1) time for the same reason as `dequeue()`.
- **empty()**: O(1) time.

### Example Usage:

```python
q = QueueFromStacks()

q.enqueue(1)
q.enqueue(2)
print(q.peek())  # Output: 1 (front of the queue is 1)
print(q.dequeue())  # Output: 1 (removes 1)
print(q.empty())  # Output: False (queue still has 2)
print(q.peek())  # Output: 2 (front of the queue is 2)
print(q.dequeue())  # Output: 2 (removes 2)
print(q.empty())  # Output: True (queue is empty)
```

### Summary:
Using two stacks to implement a queue allows us to maintain the queue's FIFO behavior, where elements are dequeued in the order they were enqueued. The key trick is transferring elements between the two stacks to reverse their order when needed. The amortized time complexity for all operations remains O(1), making this an efficient solution.
