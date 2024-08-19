### Problem Description:
You are given a 2D matrix of integers where:
- Each row is sorted in ascending order from left to right.
- Each column is sorted in ascending order from top to bottom.

Your task is to determine if a given target integer is present in the matrix.

### Example:
```plaintext
Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 30

Output: True
```

### Function Signature:
Here is the expected function signature in Python:
```python
def search_matrix(matrix: List[List[int]], target: int) -> bool:
    pass
```

### Function Calls:
```python
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 30
result = search_matrix(matrix, target)
print(result)  # Expected output: True
```

### High-Level Approach:
1. **Start from the Top-Right Corner:** The algorithm begins from the top-right corner of the matrix because this position gives a clear direction for traversal:
   - If the current element is greater than the target, move left (decrease column).
   - If the current element is less than the target, move down (increase row).
   - If the current element matches the target, return `True`.

2. **Binary Search-Like Strategy:** The matrix is sorted both row-wise and column-wise, allowing for efficient elimination of elements:
   - If the target is smaller than the current element, you know it cannot be in the current column, so you move left.
   - If the target is larger than the current element, it cannot be in the current row, so you move down.

3. **Edge Cases:**
   - Empty matrix.
   - Single row or column.
   - Target not present in the matrix.

This approach runs in `O(m + n)` time, where `m` is the number of rows and `n` is the number of columns.
