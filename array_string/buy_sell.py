'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
'''

def buy_and_sell_stock_once(prices):
        min_so_far = float('inf')
        max_profit = 0
        for i in range(len(prices)):
            min_so_far = min(min_so_far, prices[i])
            max_profit = max(max_profit, prices[i] - min_so_far)
        return max_profit
