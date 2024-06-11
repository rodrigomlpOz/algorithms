'''
Problem Statement
You are given an array prices where prices[i] is the price of a given stock on the i-th day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

'''
def maxProfit(prices):
    if not prices:
        return 0

    n = len(prices)
    left_profits = [0] * n
    right_profits = [0] * n

    # Left pass: Calculate max profit until each day
    min_price = prices[0]
    for i in range(1, n):
        min_price = min(min_price, prices[i])
        left_profits[i] = max(left_profits[i-1], prices[i] - min_price)

    # Right pass: Calculate max profit from each day to the end
    max_price = prices[-1]
    for i in range(n-2, -1, -1):
        max_price = max(max_price, prices[i])
        right_profits[i] = max(right_profits[i+1], max_price - prices[i])

    # Combine the two profits
    max_profit = 0
    for i in range(n):
        max_profit = max(max_profit, left_profits[i] + right_profits[i])

    return max_profit

# Example function calls
print(maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))  # Expected output: 6
print(maxProfit([1, 2, 3, 4, 5]))  # Expected output: 4
print(maxProfit([7, 6, 4, 3, 1]))  # Expected output: 0

