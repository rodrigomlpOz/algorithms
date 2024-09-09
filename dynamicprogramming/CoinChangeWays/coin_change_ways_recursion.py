'''
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.

 

Example 1:

Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
'''

def coin_change_ways(amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        #If we found a way to create the desired amount
        if amount == 0: 
            return 1 
        
        #If we went over our amount or we have no more coins left
        if amount < 0 or len(coins) == 0:
            return 0 

        #Our solutions can be divided into two sets,
        #   1) Solutions that cointain the coin at the end of the coins array 
        #   2) Solutions that don't contain that coin 
        return coin_change_ways(amount - coins[-1], coins) + coin_change_ways(amount, coins[:-1])
