## Problem Statement

You are given an array `prices` where `prices[i]` is the price of a given stock on the i-th day.

You want to maximize your profit by choosing two different days to buy one stock and choosing two different later days to sell those stocks. 

Return the maximum profit you can achieve from these transactions. If you cannot achieve any profit, return 0.

## Examples

- **Example 1**:
  - Input: `prices = [3, 3, 5, 0, 0, 3, 1, 4]`
  - Output: `6`
  - Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3 - 0 = 3.
    Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4 - 1 = 3.
    Total profit = 3 + 3 = 6.

- **Example 2**:
  - Input: `prices = [1, 2, 3, 4, 5]`
  - Output: `4`
  - Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5 - 1 = 4.
    No second transaction is needed as it won't provide additional profit.

- **Example 3**:
  - Input: `prices = [7, 6, 4, 3, 1]`
  - Output: `0`
  - Explanation: No transaction is done, so the maximum profit is 0.

## Function Signature

```python
def max_profit_twice(prices: list[int]) -> int:
```

## High-Level Approach

1. **First Pass (Left to Right)**:
   - Use two arrays `left_profit` and `right_profit` of the same length as `prices`.
   - Initialize variables `min_price` to track the minimum price encountered so far and `max_profit` to track the maximum profit that can be achieved for the first transaction.
   - Iterate through the prices from left to right to fill the `left_profit` array. The value at each index in `left_profit` will be the maximum profit that can be achieved if the transaction ends at or before that day.

2. **Second Pass (Right to Left)**:
   - Initialize variables `max_price` to track the maximum price encountered so far.
   - Iterate through the prices from right to left to fill the `right_profit` array. The value at each index in `right_profit` will be the maximum profit that can be achieved if the transaction starts at or after that day.

3. **Combine the Results**:
   - Iterate through the `prices` array and combine the results from `left_profit` and `right_profit` to find the maximum possible profit with two transactions. The total profit at any day is the sum of the maximum profit that can be achieved up to that day and the maximum profit that can be achieved from that day onward.

4. **Return the Result**:
   - The result will be the maximum value found in the combined results.

## Function Calls in Python

```python
# Example 1: Two profitable transactions
print(max_profit_twice([3, 3, 5, 0, 0, 3, 1, 4]))  # Expected output: 6

# Example 2: One profitable transaction
print(max_profit_twice([1, 2, 3, 4, 5]))  # Expected output: 4

# Example 3: No profitable transactions
print(max_profit_twice([7, 6, 4, 3, 1]))  # Expected output: 0

# Example 4: Two profitable transactions with varying prices
print(max_profit_twice([2, 1, 2, 0, 1]))  # Expected output: 2

# Example 5: Mixed price changes
print(max_profit_twice([6, 1, 3, 2, 4, 7]))  # Expected output: 7
```
