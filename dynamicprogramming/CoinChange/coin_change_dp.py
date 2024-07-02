class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        #amount +1 is to include the 0 column
        # coins +1 is so we dont need to have a special case in the algorithm for the first row
        
        dp = [[float('inf') for j in range(amount+1)] for i in range(len(coins)+1)]

        
        """
        M = max int value
          
				      (0 to target value)
				  0 1 2 3 4 5 6 7 8 9 10 11
          (coins)
			 0    M M M M M M M M M M M  M
			 1    0 1 2 3 4 5 6 7 8 9 10 11
			 2    0 1 1 2 2 3 3 4 4 5 6  6
			 5    0 1 1 2 3 1 2 3 3 4 2  3
        
        """
        
        #set first column to 0
        for row in range(len(dp)):
            dp[row][0] = 0
        
        
        for row in range(1, len(dp)):
            for target_value in range(len(dp[0])):
                
                coin_value = coins[row - 1]  #need to offset by one because we added extra row for float(inf) values
                
                if coin_value <= target_value:
                    dp[row][target_value] = min(dp[row][target_value - coin_value] + 1, dp[row - 1][target_value])
                else:
                    dp[row][target_value] = dp[row - 1][target_value]
                    
        
        if dp[-1][-1] == float('inf'):
            return -1
                
        return dp[-1][-1]

coins = [2]
amount = 3
ans = coin_change(coins, amount)
print(ans)
'''
Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
'''
