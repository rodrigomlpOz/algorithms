import math

def numSquares(n: int) -> int:
    # Step 1: Precompute all perfect squares up to n
    square_nums = [i**2 for i in range(1, int(math.sqrt(n)) + 1)]
    
    # Step 2: Initialize a 2D DP table
    dp = [[float('inf')] * (n + 1) for _ in range(len(square_nums) + 1)]
    
    # Base case: zero squares to form sum 0
    for i in range(len(square_nums) + 1):
        dp[i][0] = 0
    
    # Step 3: Fill the DP table
    for i in range(1, len(square_nums) + 1):
        square = square_nums[i - 1]
        for j in range(1, n + 1):
            if j >= square:
                # Min between not taking the square or taking the square
                dp[i][j] = min(dp[i - 1][j], dp[i][j - square] + 1)
            else:
                # Can't take the current square
                dp[i][j] = dp[i - 1][j]
    
    # Step 4: Return the value in dp[len(square_nums)][n]
    return dp[len(square_nums)][n]

# Example calls
print(numSquares(12))  # Output: 3
print(numSquares(13))  # Output: 2
