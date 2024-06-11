'''
Problem Statement
You are given an array prices where prices[i] is the price of a given stock on the i-th day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example
Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

'''

def buy_and_sell_stock_once(prices):
        min_so_far = float('inf')
        max_profit = 0
        for i in range(len(prices)):
            min_so_far = min(min_so_far, prices[i])
            max_profit = max(max_profit, prices[i] - min_so_far)
        return max_profit

print(buy_and_sell_stock_once([7, 1, 5, 3, 6, 4]))  # Expected output: 5
print(buy_and_sell_stock_once([7, 1, 5, 3, 6, 4]))  # Expected output: 5
print(buy_and_sell_stock_once([7, 6, 4, 3, 1]))  # Expected output: 0
