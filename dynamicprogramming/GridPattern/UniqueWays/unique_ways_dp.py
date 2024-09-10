def uniquePaths(m, n):
    # 1. Define the DP table
    dp = [[0 for _ in range(n)] for _ in range(m)]

    # 2. Initialize the base cases (first row and first column to 1)
    for i in range(m):
        dp[i][0] = 1  # Only one way to reach any cell in the first column
    for j in range(n):
        dp[0][j] = 1  # Only one way to reach any cell in the first row

    # 3. Fill the DP table using the recurrence relation
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]  # Sum of paths from top and left

    # 4. Return the result stored in dp table (bottom-right corner)
    return dp[m-1][n-1]

# Test the function
m, n = 3, 3
print(uniquePaths(m, n))  # Output: 6
