### Problem Statement:
Design a data structure, `MaxStack`, that supports the following operations efficiently:

1. **push(x)**: Push an element `x` onto the stack.
2. **pop()**: Remove the element on the top of the stack.
3. **max()**: Retrieve the maximum element currently in the stack.
4. **peek()**: Return the top element of the stack without removing it.

All of these operations should be done in **constant time**.

### Approach:
We can solve this problem by maintaining two stacks:
1. **Main Stack** (`stack`): This will handle the normal stack operations like `push` and `pop`.
2. **Max Stack** (`max_stack`): This stack will maintain the maximum values. Every time a new element is pushed onto the main stack, we also push the maximum between the new element and the current maximum onto the max stack.

### Operations:
- **push(x)**: Push `x` onto the main stack and also update the `max_stack` with the maximum between `x` and the current maximum.
- **pop()**: Pop the element from both the main stack and the max stack.
- **max()**: The maximum element is always at the top of the `max_stack`.
- **peek()**: Return the top element of the main stack.

### Function Signature:
```python
class MaxStack:
    def push(self, x):
        pass
    
    def pop(self):
        pass
    
    def max(self):
        pass
    
    def peek(self):
        pass
```

### High-Level Solution:

1. **Two Stacks**:
   - One stack (`stack`) to handle regular stack operations.
   - Another stack (`max_stack`) to track the maximum values at each point.

2. **Push Operation**:
   - When pushing `x` onto `stack`, push the maximum of `x` and the current top of `max_stack` (if `max_stack` is non-empty) onto `max_stack`.

3. **Pop Operation**:
   - When popping an element from `stack`, also pop from `max_stack` to ensure that the max value is correctly updated.

4. **Max Operation**:
   - The current maximum value is always at the top of `max_stack`.

5. **Peek Operation**:
   - Return the top element of `stack`.

### Solution Code:

```python
class MaxStack:
    def __init__(self):
        pass
    
    def push(self, x):
        # Push x onto the main stack
        pass
    
    def pop(self):
        # Pop from both stack and max_stack
        pass
    
    def max(self):
        # Return the top of the max_stack, which is the maximum element
        pass
    
    def peek(self):
        # Return the top element of the main stack
        pass
```

### Example Usage:

```python
ms = MaxStack()

# Push operations
ms.push(1)
ms.push(5)
ms.push(3)
print(ms.max())  # Output: 5 (max in [1, 5, 3])

# Pop operation
ms.pop()
print(ms.max())  # Output: 5 (max in [1, 5])

# Peek operation
print(ms.peek())  # Output: 5

# Push operation
ms.push(2)
print(ms.max())  # Output: 5 (max in [1, 5, 2])
```

### Time Complexity:
- **push(x)**: O(1), as both stacks (`stack` and `max_stack`) are updated in constant time.
- **pop()**: O(1), as elements are removed from both stacks in constant time.
- **max()**: O(1), as the maximum is always available at the top of `max_stack`.
- **peek()**: O(1), as it simply returns the top of `stack`.

### Space Complexity:
- **O(n)**, where `n` is the number of elements in the stack, since both `stack` and `max_stack` can store up to `n` elements.

This design ensures that we can retrieve the maximum element, as well as perform regular stack operations, all in constant time.
