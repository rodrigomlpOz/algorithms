## Problem Statement

You are given an array `prices` where `prices[i]` is the price of a given stock on the i-th day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

## Examples

- **Example 1**:
  - Input: `prices = [7, 1, 5, 3, 6, 4]`
  - Output: `5`
  - Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6 - 1 = 5.
  
- **Example 2**:
  - Input: `prices = [7, 6, 4, 3, 1]`
  - Output: `0`
  - Explanation: No transaction is done, so the maximum profit is 0.

## Function Signature

```python
def max_profit(prices: list[int]) -> int:
```

## High-Level Approach

1. **Initialize Variables**:
   - Use a variable `min_price` to track the minimum price encountered so far.
   - Use a variable `max_profit` to track the maximum profit that can be achieved.

2. **Iterate Through the Prices**:
   - For each price in the array, update the `min_price` if the current price is lower than the `min_price`.
   - Calculate the potential profit if the stock is sold on the current day (current price - `min_price`).
   - Update the `max_profit` if the potential profit is higher than the current `max_profit`.

3. **Return Result**:
   - After iterating through the prices, the `max_profit` will contain the maximum profit that can be achieved. If no profit can be achieved, `max_profit` will be 0.

## Function Calls in Python

```python
# Example 1: Profitable transaction
print(max_profit([7, 1, 5, 3, 6, 4]))  # Expected output: 5

# Example 2: No profitable transaction
print(max_profit([7, 6, 4, 3, 1]))  # Expected output: 0

# Example 3: Single price entry
print(max_profit([5]))  # Expected output: 0

# Example 4: Multiple price increases
print(max_profit([1, 2, 3, 4, 5]))  # Expected output: 4

# Example 5: Price dips and rises
print(max_profit([3, 2, 6, 5, 0, 3]))  # Expected output: 4
```
