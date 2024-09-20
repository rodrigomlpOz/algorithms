### Problem Statement

Design and implement an iterator to flatten a 2D vector. The iterator should support the `next` and `hasNext` methods.

The `Vector2D` class will be initialized with a 2D vector `v` and should provide the following methods:

1. `next()`: Returns the next element in the 2D vector and moves the iterator to the following element.
2. `hasNext()`: Returns a boolean indicating whether there are more elements to iterate over in the 2D vector.

### Example

```python

class Vector2D:
    def __init__(self, v: List[List[int]]):
        pass

    def next(self) -> int:
        pass

    def hasNext(self) -> bool:
        pass


v = [
    [1, 2],
    [3],
    [4, 5, 6]
]
i = Vector2D(v)
result = []
while i.hasNext():
    result.append(i.next())
print(result)  # Output: [1, 2, 3, 4, 5, 6]
```

### High-Level Approach

1. **Initialization**:
   - Initialize the class with the 2D vector `v`.
   - Set pointers `outer` and `inner` to keep track of the current position in the 2D vector. `outer` tracks the row, and `inner` tracks the column within the row.

2. **Advance to Next Valid Element**:
   - Create a method `advance_to_next` to move the pointers to the next valid element in the 2D vector.
   - The method iterates through the rows and columns until it finds a non-empty list or reaches the end of the 2D vector.

3. **Next Element**:
   - The `next` method uses `advance_to_next` to ensure it points to a valid element.
   - It returns the current element and moves the `inner` pointer to the next position.

4. **Check for Next Element**:
   - The `hasNext` method also uses `advance_to_next` to check if there is any remaining element.
   - It returns `True` if there are more elements to iterate over and `False` otherwise.
