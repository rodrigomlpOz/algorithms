### Problem: 155. Min Stack

**Problem Statement:**
Design a stack that supports the following operations in constant time:
1. `push(val)`: Pushes the element `val` onto the stack.
2. `pop()`: Removes the element on the top of the stack.
3. `top()`: Retrieves the top element of the stack.
4. `getMin()`: Retrieves the minimum element in the stack.

You need to implement the `MinStack` class, where all the operations should have **O(1)** time complexity.

### Class Definition:

```python
class MinStack:
    def __init__(self):
        """
        Initialize the MinStack object.
        """
        pass
    
    def push(self, val: int) -> None:
        """
        Pushes the element val onto the stack.
        """
        pass
    
    def pop(self) -> None:
        """
        Removes the element on the top of the stack.
        """
        pass
    
    def top(self) -> int:
        """
        Gets the top element of the stack.
        """
        pass
    
    def getMin(self) -> int:
        """
        Retrieves the minimum element in the stack.
        """
        pass
```

### Function Calls:

```python
# Initialize the stack
minStack = MinStack()

# Test Case 1: Push values onto the stack
minStack.push(-2)
minStack.push(0)
minStack.push(-3)

# Get the minimum element
print(minStack.getMin())  # Expected Output: -3

# Pop the top value
minStack.pop()

# Get the top value
print(minStack.top())  # Expected Output: 0

# Get the minimum element after popping
print(minStack.getMin())  # Expected Output: -2
```

### High-Level Solution:

To implement the `MinStack` class with O(1) time complexity for each operation, we need to manage two things:
1. **Main Stack:** To store the actual stack elements.
2. **Min Stack:** To store the minimum value at each point in time. This ensures that when we pop an element from the main stack, we can still access the current minimum element in constant time.

#### Key Insights:
- Each time we `push` an element onto the main stack, we also push the minimum element (either the new element or the current minimum) onto the `minStack`.
- When popping from the main stack, we pop from the `minStack` as well, ensuring the top of the `minStack` always holds the current minimum value.
- This allows constant-time retrieval of the minimum value.

### Full Implementation:

```python
class MinStack:
    def __init__(self):
        # Initialize the main stack and a stack to keep track of the minimum values
        pass
    
    def push(self, val: int) -> None:
        # Push the value onto the main stack
        pass
    
    def pop(self) -> None:
        # Pop the top element from both the main stack and the minStack
        pass
    
    def top(self) -> int:
        # Return the top element of the main stack
        pass
    
    def getMin(self) -> int:
        # Return the top element of the minStack, which is the current minimum
        pass
```

### Explanation of the Solution:

1. **Main Stack (`self.stack`):** 
   - This stack stores the actual values being pushed onto the stack.

2. **Min Stack (`self.minStack`):** 
   - This auxiliary stack tracks the minimum element at each level of the main stack. The top of `minStack` always holds the current minimum element in the stack.

3. **Push Operation:**
   - When pushing a value onto the stack, we also push the current minimum value onto the `minStack`.
   - If the `minStack` is empty, the current value is pushed.
   - If the `minStack` is not empty, we compare the current value with the top of the `minStack` and push the smaller one.

4. **Pop Operation:**
   - When popping from the stack, we pop the value from both the `stack` and `minStack`, ensuring the `minStack` still holds the correct minimum.

5. **Top Operation:**
   - The `top()` function simply returns the top element of the main stack.

6. **GetMin Operation:**
   - The `getMin()` function returns the top element of the `minStack`, which is always the current minimum element.

### Example:

```python
# Initialize the stack
minStack = MinStack()

# Push values onto the stack
minStack.push(-2)
minStack.push(0)
minStack.push(-3)

# Get the minimum element
print(minStack.getMin())  # Output: -3

# Pop the top value
minStack.pop()

# Get the top value
print(minStack.top())  # Output: 0

# Get the minimum element after popping
print(minStack.getMin())  # Output: -2
```

### Time and Space Complexity:
- **Time Complexity:** O(1) for `push()`, `pop()`, `top()`, and `getMin()` since each operation only involves a single action (push, pop, or accessing the top element).
- **Space Complexity:** O(n), where `n` is the number of elements in the stack. The space is used to store both the main stack and the min stack. In the worst case, both stacks will have the same number of elements.