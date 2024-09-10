### Problem Statement:
You are given an `m x n` grid filled with non-negative numbers. Your task is to find a path from the top-left corner to the bottom-right corner of the grid that minimizes the sum of all numbers along its path. You can only move either down or right at any point in time.

### Function Definition:
```python
def minPathSum(grid: List[List[int]]) -> int:
    """
    Given a 2D grid filled with non-negative numbers, this function returns the minimum 
    path sum from the top-left corner to the bottom-right corner.
    
    Args:
    grid: List[List[int]] - A 2D list representing the grid with non-negative numbers.
    
    Returns:
    int - The minimum sum possible by moving from the top-left to the bottom-right corner.
    """
```

### Function Calls:
```python
# Test case 1: A small grid
grid1 = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]
print(minPathSum(grid1))  # Expected output: 7 (1 → 3 → 1 → 1 → 1)

# Test case 2: A single row grid
grid2 = [
    [1, 2, 3]
]
print(minPathSum(grid2))  # Expected output: 6 (1 → 2 → 3)

# Test case 3: A single column grid
grid3 = [
    [1],
    [2],
    [3]
]
print(minPathSum(grid3))  # Expected output: 6 (1 → 2 → 3)

# Test case 4: Larger grid
grid4 = [
    [1, 2, 5],
    [3, 2, 1]
]
print(minPathSum(grid4))  # Expected output: 6 (1 → 2 → 2 → 1)
```

### High-Level Solution:
The idea is to use **dynamic programming (DP)** to solve the problem by modifying the grid in-place. We start from the top-left corner and move towards the bottom-right, updating each cell with the minimum sum required to reach that cell.

Here’s the high-level approach:

1. **Base Case**: 
   - If there is only one cell, the minimum path sum is simply the value of that cell.
   - If there’s only one row or one column, the path is straightforward: either move right for a row or down for a column.

2. **Dynamic Programming Approach**:
   - We use the grid itself to store the minimum sum to reach each cell, modifying it as we go. 
   - For each cell `(i, j)` in the grid, the minimum sum to reach that cell is the minimum of:
     - The sum to reach the cell directly above it (`grid[i-1][j]`), if `i > 0`.
     - The sum to reach the cell directly to its left (`grid[i][j-1]`), if `j > 0`.
   - Add the minimum of those two to the current cell value `grid[i][j]`.

3. **Final Answer**:
   - The value at the bottom-right corner of the grid will hold the minimum sum to reach that cell from the top-left corner.

### Time Complexity:
- **O(m * n)**, where `m` is the number of rows and `n` is the number of columns in the grid. We iterate over every cell once.

### Space Complexity:
- **O(1)** if we modify the grid in-place. Otherwise, **O(m * n)** if we use a separate DP table.


### Explanation:

1. **First row and column**: We update the first row and column separately, as they can only be reached from one direction (either left for rows or above for columns).
2. **Rest of the grid**: For each remaining cell, the minimum path to that cell is the smaller of the two possible paths (from the top or from the left).
3. **Result**: Once the grid is filled, the bottom-right corner holds the minimum path sum from the top-left to the bottom-right.

Let me know if you'd like more clarification or further details on this approach!
