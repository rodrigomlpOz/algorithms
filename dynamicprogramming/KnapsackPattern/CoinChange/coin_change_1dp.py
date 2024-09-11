def coinChange2(coins, amount):
    # Step 1: Initialize the DP array
    dp = [0] * (amount + 1)
    
    # Step 2: Base case: There is one way to make the amount 0
    dp[0] = 1

    # Step 3: Iterate over each amount from 1 to 'amount'
    for i in range(1, amount + 1):
        # Step 4: For each amount i, check all coin denominations
        for coin in coins:
            if i >= coin:
                # Step 5: Update dp[i] with the number of ways to make amount i
                dp[i] += dp[i - coin]

    # Step 6: Return the number of ways to make the amount
    return dp[amount]

# Example usage
print(coinChange2([1, 2, 5], 5))  # Output: 4
