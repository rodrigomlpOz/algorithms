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
