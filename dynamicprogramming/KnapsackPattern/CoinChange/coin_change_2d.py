def coinChange2D(coins, amount):
    n = len(coins)
    
    # Initialize a 2D DP array with dimensions (n+1) x (amount+1)
    dp = [[float('inf')] * (amount + 1) for _ in range(n + 1)]
    
    # Base case: It takes 0 coins to make amount 0
    for i in range(n + 1):
        dp[i][0] = 0
    
    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(1, amount + 1):
            # If the coin value is greater than the current amount j, we exclude the coin
            if j < coins[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                # Either we exclude the coin or include it (1 + dp[i][j - coins[i-1]])
                dp[i][j] = min(dp[i - 1][j], 1 + dp[i][j - coins[i - 1]])
    
    # If dp[n][amount] is infinity, return -1 (no solution), otherwise return dp[n][amount]
    return dp[n][amount] if dp[n][amount] != float('inf') else -1

# Example usage:
print(coinChange2D([1, 2, 5], 11))  # Output: 3 (11 = 5 + 5 + 1)
