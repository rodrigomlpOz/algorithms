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

