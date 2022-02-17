'''
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
'''

def coin_change(arr, amount):
    def recurse(arr, amount):
        if amount < 0:
            return float('inf')
        if amount == 0:
            return 0
        else:
            min_val = float('inf')
            for i in range(len(arr)):
                if arr[i] > amount:
                    break 
                curr_val = 1 + recurse(arr, amount - arr[i])
                min_val = min(min_val, curr_val)
        return min_val 
    ans = recurse(arr, amount)
    return -1 if ans == float('inf') else ans

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
