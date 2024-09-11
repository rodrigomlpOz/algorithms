### Coin Change Problem Description:

You are given an integer array `coins` representing different denominations of coins and an integer `amount` representing a total amount of money. Your goal is to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return `-1`.

You may assume that you have an infinite number of each coin.

### Function Definition:

```python
def coinChange(coins: List[int], amount: int) -> int:
    """
    Function to determine the minimum number of coins needed to make up a given amount.

    Args:
    coins : List[int] : A list of coin denominations.
    amount : int : The total amount of money.

    Returns:
    int : The minimum number of coins needed to make up the given amount, or -1 if it's not possible.
    """
```

### Example Calls:

```python
coins = [1, 2, 5]
amount = 11
print(coinChange(coins, amount))  # Expected output: 3 (11 = 5 + 5 + 1)

coins = [2]
amount = 3
print(coinChange(coins, amount))  # Expected output: -1 (It's not possible to make 3 with only 2)

coins = [1]
amount = 0
print(coinChange(coins, amount))  # Expected output: 0 (No coins are needed for amount 0)
```

### High-Level Solution:

The problem can be solved using dynamic programming (DP). The idea is to build an array `dp` where `dp[i]` represents the minimum number of coins needed to make the amount `i`. Here’s the approach:

1. **Initialization**:  
   - Create a DP array `dp` of size `amount + 1` initialized to infinity (`float('inf')`) to represent unreachable amounts. Set `dp[0] = 0`, since 0 coins are needed to make amount 0.

2. **DP Array Calculation**:  
   - For each coin in `coins`, update the DP array by checking if we can make the current amount `i` using the current coin. If using the coin results in a lower number of coins, update `dp[i]`.

3. **Return Result**:  
   - After filling the DP array, if `dp[amount]` is still `float('inf')`, return `-1` (it’s not possible to make the amount). Otherwise, return `dp[amount]`, which will contain the minimum number of coins needed.

### Explanation:

- **Initialization**: `dp[0] = 0` because no coins are required to make amount 0.
- **DP Transition**: For each coin, if it fits into the current amount `i`, check if using it reduces the number of coins needed.
- **Result**: After processing, if `dp[amount]` is still infinity, it means the amount cannot be made with the given coins, so return `-1`. Otherwise, return the value at `dp[amount]`, which is the minimum number of coins needed.