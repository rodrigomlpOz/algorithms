### Problem Statement:
Determine if a given `9 x 9` Sudoku board is valid. The board may be partially filled, where an empty cell is represented by the character `'.'`.

A valid Sudoku board must satisfy the following rules:
1. Each row must contain the digits `1-9` without repetition.
2. Each column must contain the digits `1-9` without repetition.
3. Each of the nine `3x3` sub-boxes of the grid must contain the digits `1-9` without repetition.

The board can be partially filled, but any existing number must respect the Sudoku rules.

### Function Definition:
```python
def is_valid_sudoku(board: list[list[str]]) -> bool:
    # Function to determine if a given Sudoku board is valid
```

### Function Call Example:
```python
board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
print(is_valid_sudoku(board))  # Output: True
```

### High-Level Description:
1. **Objective**: To validate whether the given `9 x 9` Sudoku board follows the Sudoku rules.
2. **Approach**:
   - Create 3 sets of collections for tracking the values:
     1. **Rows**: A list of sets where each set tracks the numbers encountered in that row.
     2. **Columns**: A list of sets where each set tracks the numbers encountered in that column.
     3. **Sub-grids**: A list of sets where each set tracks the numbers encountered in that `3x3` sub-box.
   - Traverse the board, and for each number encountered (not `'.'`), check:
     1. If the number has already appeared in the corresponding row, column, or sub-grid.
     2. If the number is valid (not repeating), add it to the corresponding row, column, and sub-grid.
   - Return `False` if any rule is violated; otherwise, return `True`.
3. **Efficiency**:
   - Time Complexity: O(1), since the board is always `9x9`.
   - Space Complexity: O(1), constant space since the size of the grid is fixed.

### Code Implementation:
```python
def is_valid_sudoku(board: list[list[str]]) -> bool:
    # Initialize sets to track the numbers in rows, columns, and sub-boxes
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    sub_boxes = [set() for _ in range(9)]
    
    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num == '.':
                continue
            
            # Determine sub-box index
            sub_box_index = (i // 3) * 3 + (j // 3)
            
            # Check if the number is already in the row, column, or sub-box
            if num in rows[i] or num in cols[j] or num in sub_boxes[sub_box_index]:
                return False
            
            # Add the number to the corresponding row, column, and sub-box
            rows[i].add(num)
            cols[j].add(num)
            sub_boxes[sub_box_index].add(num)
    
    # If no rule is violated, return True
    return True
```

### Explanation of the Code:
1. **Rows, Columns, and Sub-boxes**: Three lists of sets are created to store numbers encountered in each row, column, and sub-grid, respectively.
2. **Sub-box Index Calculation**: The sub-box is identified by dividing the row and column indices by 3, then calculating the corresponding box using `(i // 3) * 3 + (j // 3)`.
3. **Validation**: For each number in the board, we check if it has already been added to its respective row, column, or sub-grid. If so, return `False`. Otherwise, add the number to the appropriate sets.

### Example Walkthrough:

For the given board:
```python
board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
```

- The function checks each number in the board and verifies that it follows the Sudoku rules. For this example, the board is valid, and the output will be `True`.
