'''
Grea explanation of this approach
https://www.youtube.com/watch?v=DJ4a7cmjZY0

M after processing coin 3:
1 1 1 1 1 1
1 1 2 2 3 3
1 1 2 2 3 3
1 1 2 2 3 4
'''
class Solution:
    def change(self, amount, coins):
        num_coins = len(coins)  # Number of different coin types
        # Initialize a DP table with dimensions (num_coins + 1) x (amount + 1)
        dp_table = [[0 for _ in range(amount + 1)] for _ in range(num_coins + 1)]
        
        # There is exactly one way to make the amount 0: use no coins
        for i in range(num_coins + 1):
            dp_table[i][0] = 1
        
        # Fill the DP table
        for i in range(1, num_coins + 1):
            for j in range(1, amount + 1):
                # If the current coin's value is greater than the current amount,
                # we cannot use this coin, so we inherit the value from the row above
                if coins[i - 1] > j:
                    dp_table[i][j] = dp_table[i - 1][j]
                else:
                    # Otherwise, we consider the ways without this coin (dp_table[i-1][j])
                    # and the ways including this coin (dp_table[i][j - coins[i-1]])
                    dp_table[i][j] = dp_table[i - 1][j] + dp_table[i][j - coins[i - 1]]
        
        # The answer is the number of ways to make the amount using all the given coins
        return dp_table[num_coins][amount]

# Example usage
sol = Solution()
amount = 5
coins = [1, 2, 5]
print(sol.change(amount, coins))  # Output: 4

