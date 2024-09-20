### Problem Statement:

Given an `m x n` matrix, if an element is `0`, set its entire row and column to `0`. You must do this **in-place** (without using extra space for another matrix).

### Constraints:
1. You should not allocate another 2D matrix to perform the operation.
2. Try to solve the problem with constant space complexity, although a solution with `O(m + n)` extra space is also acceptable initially.

### Function Definition:

```python
def setZeroes(matrix: List[List[int]]) -> None:
    """
    Modify the input matrix in-place. If any element is 0, set its entire row and column to 0.
    
    :param matrix: List[List[int]] - The input 2D matrix
    :return: None - The matrix is modified in-place
    """
    is_zero_row = False
    is_zero_col = False
    #check first col
    for i in range(len(matrix)):
        if matrix[i][0] == 0:
            is_zero_col = 0
    
    for j in range(len(matrix[0])):
        if matrix[0][j] == 0:
            is_zero_row = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] = 0:
                matrix[0][j] = 0
                matrix[i][0] = 0

    #check first col
    for i in range(1, len(matrix)):
        if matrix[i][0] == 0:
            for j in range(0, len(matrix[0])):
                matrix[i][j] = 0

    for j in range(1, len(matrix)):
        if matrix[0][j] == 0:
            for i in range(0, len(matrix)):
                matrix[i][j] = 0
        


    #check first col


matrix = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]
setZeroes(matrix)

matrix = [
    [0, 2, 3],
    [4, 5, 0],
    [7, 8, 9]
]
setZeroes(matrix)
```

### High-Level Description:

To solve this problem, we can approach it in two ways:

1. **Brute Force Approach** (Using O(m + n) extra space):
   - First, iterate through the matrix to find all the cells that contain a `0`. Store the indices of these rows and columns in separate sets.
   - In a second pass, iterate over the matrix again. For every row and column stored in the sets, set the entire row and column to `0`.
   - This approach uses additional space proportional to the number of rows and columns (`O(m + n)`).

2. **Optimal Approach** (In-place with constant space):
   - Instead of using additional space to track rows and columns, we can use the first row and first column of the matrix as markers.
   - We traverse the matrix and for every `0` found at `matrix[i][j]`, we mark `matrix[0][j] = 0` (to mark the column) and `matrix[i][0] = 0` (to mark the row).
   - After marking, we use this information to set the appropriate rows and columns to `0`.
   - Finally, handle the first row and first column separately, because they were used as markers.

### Code Implementation:

```python

```

### High-Level Steps:

1. **Step 1 (Detect the Zeroes in First Row and Column):**
   - We first check whether the first row and the first column contain any zeroes. This is necessary because they will be used as markers, and if they contain zeroes, the entire first row or column needs to be zeroed later.

2. **Step 2 (Marking Rows and Columns):**
   - Traverse the rest of the matrix (excluding the first row and column). If we encounter a zero at `matrix[i][j]`, we mark the first element of the row (`matrix[i][0]`) and the first element of the column (`matrix[0][j]`) as `0`. This marks the row and column that need to be zeroed out later.

3. **Step 3 (Set Zeroes Based on Markers):**
   - Use the markers in the first row and column to set the corresponding rows and columns to zero.

4. **Step 4 (Handle the First Row and First Column Separately):**
   - If the first row or column was initially marked to be zeroed (from step 1), zero out the entire first row or first column.

### Function Calls:

#### Example 1:
```python
matrix = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]
setZeroes(matrix)
print(matrix)  # Output: [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
```

#### Example 2:
```python
matrix = [
    [0, 1, 2, 0],
    [3, 4, 5, 2],
    [1, 3, 1, 5]
]
setZeroes(matrix)
print(matrix)  # Output: [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
```

### Time and Space Complexity:

- **Time Complexity:** `O(m * n)`, where `m` is the number of rows and `n` is the number of columns. We traverse the matrix twice.
- **Space Complexity:** `O(1)` (constant space), as we only use a few extra variables and modify the matrix in place.
