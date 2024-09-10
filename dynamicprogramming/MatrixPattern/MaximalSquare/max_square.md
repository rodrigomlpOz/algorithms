### Problem: **Maximal Square**

**Problem Statement:**

Given a 2D binary matrix filled with `'0'` and `'1'`, find the largest square containing only `1`s and return its area.

### Example:

```plaintext
Input:
matrix = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 4
Explanation: The largest square containing only 1's has a side length of 2, so the area is 4.
```

---

### Function Definition:

```python
class Solution:
    def maximalSquare(self, matrix):
        """
        Function to find the largest square containing only '1's in a binary matrix.
        
        Args:
        matrix: List[List[str]] - 2D binary matrix containing '0's and '1's.
        
        Returns:
        int - Area of the largest square that contains only '1's.
        """
```

---

### High-Level Solution:

We can solve the **Maximal Square** problem using **dynamic programming (DP)**. The idea is to use a DP table to store the size of the largest square that ends at each cell in the matrix. If a cell contains a `'1'`, then the size of the square ending at that cell will be the minimum of the squares that end to its left, top, and top-left, plus 1.

#### Key Steps:
1. **Initialization**:
   - Create a DP table with dimensions `(rows + 1) x (cols + 1)` initialized to `0`. The extra row and column are added to simplify boundary condition checks.
   
2. **DP Transition**:
   - For each cell in the matrix that contains a `'1'`, update the corresponding cell in the DP table:
     \[
     dp[r+1][c+1] = \min(dp[r][c], dp[r+1][c], dp[r][c+1]) + 1
     \]
   - This formula calculates the size of the largest square that ends at `(r+1, c+1)` by looking at the neighboring cells to its top, left, and top-left.

3. **Track the Largest Square**:
   - While filling the DP table, keep track of the size of the largest square (`max_side`). At the end, the area of the largest square is `max_side^2`.

### Time Complexity:
- **O(m * n)**, where `m` is the number of rows and `n` is the number of columns in the matrix. We iterate over all cells once.

### Space Complexity:
- **O(m * n)**, where `m` is the number of rows and `n` is the number of columns in the matrix. We use a DP table of size `(m+1) x (n+1)`.

---

### Function Calls:

```python
# Example 1
matrix = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
solution = Solution()
print(solution.maximalSquare(matrix))  # Output: 4

# Example 2
matrix = [
  ["0","1"],
  ["1","0"]
]
print(solution.maximalSquare(matrix))  # Output: 1

# Example 3
matrix = [
  ["0"]
]
print(solution.maximalSquare(matrix))  # Output: 0
```

### Explanation:
- **DP Table**: The DP table keeps track of the largest square that ends at each cell. If the cell in the original matrix contains a `'1'`, the value in the DP table at `(r+1, c+1)` is the size of the largest square ending at that point.
- **Max Side**: As we fill the DP table, we keep track of the largest square found, which allows us to calculate the area by squaring the side length.

---

This approach efficiently finds the area of the largest square in the binary matrix by using a dynamic programming solution with minimal overhead.