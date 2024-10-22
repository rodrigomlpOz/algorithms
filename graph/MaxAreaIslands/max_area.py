def max_area_of_island(grid):
    """
    Given a 2D grid, returns the maximum area of an island.
    
    Args:
    grid (List[List[int]]): A 2D list where 1 represents land and 0 represents water.

    Returns:
    int: The area of the largest island.
    """
    # Directions arrays to move in 4 possible directions (up, down, left, right)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    def dfs(x, y):
        # Check for out-of-bounds or water
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 0:
            return 0
        
        # Mark the cell as visited
        grid[x][y] = 0
        area = 1
        
        # Explore all 4 possible directions
        for direction in directions:
            next_x, next_y = x + direction[0], y + direction[1]
            area += dfs(next_x, next_y)
        
        return area
    
    max_area = 0
    
    # Iterate through the grid to find islands
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                # Calculate the area of the connected island and update max_area
                max_area = max(max_area, dfs(i, j))
    
    return max_area

# Example 1:
grid1 = [
    [0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 1, 0, 0],
    [1, 0, 0, 0, 1]
]
print(max_area_of_island(grid1))  # Expected output: 5

# Example 2:
grid2 = [
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
print(max_area_of_island(grid2))  # Expected output: 0
