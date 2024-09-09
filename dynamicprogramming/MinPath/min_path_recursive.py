def minPathSum(grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])

    def helper(i, j):
        # Base case: if we're at the bottom-right corner, return its value
        if i == rows - 1 and j == cols - 1:
            return grid[i][j]
        
        # If we're out of bounds, return a very large number (invalid path)
        if i >= rows or j >= cols:
            return float('inf')
        
        # Recursively calculate the minimum path sum by moving right and down
        right = helper(i, j + 1)
        down = helper(i + 1, j)
        
        # Return the current cell value plus the minimum of right or down paths
        return grid[i][j] + min(right, down)
    
    # Start recursion from the top-left corner
    return helper(0, 0)
