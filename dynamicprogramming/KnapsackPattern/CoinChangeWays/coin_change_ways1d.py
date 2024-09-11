  def change(self, amount, coins):
      # Initialize a 1D DP array with size (amount + 1), and set dp[0] to 1
      dp = [0] * (amount + 1)
      dp[0] = 1  # There's one way to make amount 0 (use no coins)
      
      # Process each coin
      for coin in coins:
          for j in range(coin, amount + 1):
              dp[j] += dp[j - coin]  # Add ways to make amount j by including this coin
      
      # The answer is the number of ways to make the amount using all the coins
      return dp[amount]

amount = 5
coins = [1, 2, 5]
print(change(amount, coins))  # Output: 4
