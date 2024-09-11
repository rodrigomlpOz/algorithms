def coinChange(coins, amount):
    # Step 1: Initialize the DP array
    dp = [float('inf')] * (amount + 1)
    
    # Step 2: Base case: 0 coins are needed to make amount 0
    dp[0] = 0

    # Step 3: Iterate over each amount from 1 to 'amount'
    for i in range(1, amount + 1):
        # Step 4: For each amount i, check all coin denominations
        for coin in coins:
            if i >= coin:
                # Step 5: Update dp[i] with the minimum number of coins
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # Step 6: If dp[amount] is still infinity, return -1 (no solution), otherwise return dp[amount]
    return dp[amount] if dp[amount] != float('inf') else -1

# Example usage
print(coinChange([1, 2, 5], 11))  # Output: 3 (11 = 5 + 5 + 1)
