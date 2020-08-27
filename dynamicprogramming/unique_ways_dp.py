def unique_paths(m, n):
    grid = [[0]*m for i in range(n) ]
    for i in range(m):
        grid[0][i] = 1
    for j in range(n):
        grid[j][0] = 1
    for i in range(1, n):
        for j in range(1, m):
            grid[i][j] += (grid[i-1][j] + grid[i][j-1])
    return grid[n-1][m-1]
        
m = 7
n = 3
r = unique_paths(m, n)
print(r)