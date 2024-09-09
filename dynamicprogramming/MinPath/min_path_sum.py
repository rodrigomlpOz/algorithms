def minPathSum(grid: List[List[int]]) -> int:
    # Get the number of rows and columns
    rows, cols = len(grid), len(grid[0])
    
    # Update the first row (can only come from the left)
    for j in range(1, cols):
        grid[0][j] += grid[0][j - 1]
    
    # Update the first column (can only come from above)
    for i in range(1, rows):
        grid[i][0] += grid[i - 1][0]
    
    # Fill in the rest of the grid with the minimum path sum
    for i in range(1, rows):
        for j in range(1, cols):
            grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
    
    # The answer is now at the bottom-right corner of the grid
    return grid[rows - 1][cols - 1]
