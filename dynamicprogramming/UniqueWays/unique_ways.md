Here’s the breakdown for solving the **unique paths** problem using a recursive approach:

### Problem Description:
Given an `m x n` grid, you are located at the top-left corner, and you need to move to the bottom-right corner. You can only move either **right** or **down** at any step. The task is to find how many unique paths exist from the top-left corner to the bottom-right corner.

### Function Definition:
```python
def uniquePaths(m, n):
    """
    Recursive function to calculate the number of unique paths in an m x n grid.

    Args:
    m : int : The number of rows in the grid.
    n : int : The number of columns in the grid.

    Returns:
    int : The number of unique paths from the top-left to the bottom-right corner.
    """
    # Base case and recursive logic to be added below
    pass
```

### Function Calls:
```python
# Example calls to test the recursive function

# For a 3x3 grid
m = 3
n = 3
print(uniquePaths(m, n))  # Expected output: 6

# For a 2x2 grid
m = 2
n = 2
print(uniquePaths(m, n))  # Expected output: 2

# For a 3x2 grid
m = 3
n = 2
print(uniquePaths(m, n))  # Expected output: 3
```

### High-Level Solution:

The problem can be broken down recursively. If you are at any cell `(i, j)`, you can either:
1. Move **right** to the cell `(i, j+1)`.
2. Move **down** to the cell `(i+1, j)`.

Thus, the total number of unique paths to the bottom-right corner from `(i, j)` is the sum of the unique paths from the cell to the right `(i, j+1)` and the cell below `(i+1, j)`.

#### Recursive Formula:

Let `uniquePaths(m, n)` represent the number of unique paths to reach the bottom-right corner of a grid of size `m x n`. The recursive relation is:

\[ \text{uniquePaths}(m, n) = \text{uniquePaths}(m-1, n) + \text{uniquePaths}(m, n-1) \]

Where:
- `uniquePaths(m-1, n)` represents the number of unique paths from the cell above.
- `uniquePaths(m, n-1)` represents the number of unique paths from the cell to the left.

#### Base Case:
- If there's only one row (`m == 1`), or only one column (`n == 1`), there is only **one unique path**, either all the way right or all the way down.
  \[ \text{uniquePaths}(1, n) = 1 \]
  \[ \text{uniquePaths}(m, 1) = 1 \]

### Recursive Function with Base Case:
```python
def uniquePaths(m, n):
    # Base Case: If there's only one row or one column, there's only one path
    if m == 1 or n == 1:
        return 1

    # Recursive case: The total number of unique paths is the sum of:
    # 1. Paths from the cell above (m-1, n)
    # 2. Paths from the cell to the left (m, n-1)
    return uniquePaths(m - 1, n) + uniquePaths(m, n - 1)

# Example calls
m = 3
n = 3
print(uniquePaths(m, n))  # Output: 6
```

### Example Walkthrough:

For a `3x3` grid, the function calls break down like this:

```
uniquePaths(3, 3)
    -> uniquePaths(2, 3) + uniquePaths(3, 2)
        -> (uniquePaths(1, 3) + uniquePaths(2, 2)) + (uniquePaths(2, 2) + uniquePaths(3, 1))
            -> uniquePaths(2, 2) further breaks down until the base cases are reached
```

### Time Complexity:
This recursive solution has a **time complexity of O(2^(m + n))**, since the same subproblems are recomputed multiple times. To optimize this, you would need to apply **memoization** or **dynamic programming** to store intermediate results and avoid recomputation.

Let me know if you need further clarification!
