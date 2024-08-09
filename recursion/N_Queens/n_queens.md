## Problem Statement

The N-Queens problem involves placing N chess queens on an N×N chessboard so that no two queens threaten each other. A solution must ensure that no two queens share the same row, column, or diagonal. The output should be a binary matrix where `1` indicates the position of a queen and `0` represents an empty space.

## Function Signature

```python

def solveNQ(): 
    board = [ [0, 0, 0, 0], 
              [0, 0, 0, 0], 
              [0, 0, 0, 0], 
              [0, 0, 0, 0] ] 
  
    if solveNQUtil(board, 0) == False: 
        print ("Solution does not exist") 
        return False
  
    printSolution(board) 
    return True
  
# Driver Code 
solveNQ() 
```

### Supporting Functions

1. **`isSafe(board, row, col)`**: Checks if a queen can be safely placed at `board[row][col]`.
2. **`solveNQUtil(board, col)`**: Utilizes backtracking to place queens on the board starting from the leftmost column.

### Input

- No explicit input is required since `N` is predefined.

### Output

- The function should output a binary matrix representing a solution where queens are placed.

## High-Level Approach

1. **Backtracking**: Use backtracking to explore potential placements of queens on the board. If placing a queen in a certain position leads to a solution, the function proceeds. If not, it backtracks and tries the next possible position.

2. **Safety Check**: The `isSafe` function checks:
   - **Row Check**: No queen should already be placed in the same row.
   - **Upper Diagonal Check**: No queen should be present on the upper diagonal.
   - **Lower Diagonal Check**: No queen should be present on the lower diagonal.

3. **Recursive Solution Building**: The `solveNQUtil` function attempts to place queens column by column. If placing a queen in a particular column and row is safe, it recursively attempts to place the next queen. If successful, the function returns `True`; otherwise, it removes the queen (backtracks) and tries the next position.

4. **Output**: The `solveNQ` function initializes the board and invokes the utility function. If a solution is found, it prints the board; otherwise, it indicates that no solution exists.

### Function Calls and Example

Here is an example of how the function can be called and the expected output for `N = 4`:

```python
solveNQ()
```

**Expected Output:**

```
0 1 0 0 
0 0 0 1 
1 0 0 0 
0 0 1 0 
```

In this example, the output matrix indicates one of the possible solutions to the 4-Queens problem, with `1` representing the positions of the queens.
