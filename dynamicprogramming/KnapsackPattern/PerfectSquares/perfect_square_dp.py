import math

def numSquares(n: int) -> int:
    # DP array to store the least number of perfect squares for each value up to n
    dp = [float('inf')] * (n + 1)
    dp[0] = 0  # base case: 0 can be represented by 0 squares

    # Precompute all square numbers up to n
    square_nums = [i**2 for i in range(1, int(math.sqrt(n)) + 1)]
    
    # Fill the DP array
    for i in range(1, n + 1):
        for square in square_nums:
            if i < square:
                break
            dp[i] = min(dp[i], dp[i - square] + 1)
    
    return dp[n]

# Example calls
print(numSquares(12))  # Output: 3
print(numSquares(13))  # Output: 2
