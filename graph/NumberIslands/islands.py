def numIslands(grid):
    if not grid:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    visited = set()  # Set to track visited cells
    
    def dfs(r, c):
        # Base case: if we're out of bounds or at a water cell or already visited
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0' or (r, c) in visited:
            return
        
        visited.add((r, c))  # Mark the current cell as visited
        
        # Visit all neighboring cells (up, down, left, right)
        dfs(r - 1, c)
        dfs(r + 1, c)
        dfs(r, c - 1)
        dfs(r, c + 1)
    
    num_islands = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and (r, c) not in visited:
                dfs(r, c)  # Perform DFS to mark the entire island
                num_islands += 1  # Increase the island count
    
    return num_islands
