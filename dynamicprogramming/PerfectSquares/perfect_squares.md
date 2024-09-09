### Problem Statement:

Given an integer `n`, your task is to find the least number of perfect square numbers (for example, `1, 4, 9, 16, ...`) which sum to `n`.

For example:
- If `n = 12`, the output should be `3` because `12 = 4 + 4 + 4`.
- If `n = 13`, the output should be `2` because `13 = 4 + 9`.

### Function Definition:

```python
def numSquares(n: int) -> int:
    # Function to calculate the least number of perfect square numbers that sum to n
    pass
```

### Function Calls Example:

```python
# Example 1
n = 12
print(numSquares(n))  # Output: 3

# Example 2
n = 13
print(numSquares(n))  # Output: 2
```

### High-Level Solution:

1. **Identify the Problem:** 
   The problem can be solved by breaking down `n` into perfect squares. We want to minimize the number of perfect squares that sum to `n`.

2. **Use Dynamic Programming (DP):**
   We'll use dynamic programming to avoid recalculating values for the same inputs and reduce redundant work. The key idea is to use a DP array where each index `i` stores the minimum number of perfect squares needed to sum to `i`.

3. **Steps:**
   - **Initialization:** Create a DP array of size `n+1` initialized to infinity (`inf`), except for `dp[0] = 0` (because 0 can be represented by 0 squares).
   - **Generate all square numbers** less than or equal to `n`.
   - **Iterate through all numbers** from 1 to `n`, and for each number `i`, check all perfect square numbers less than `i` and update the DP array accordingly.
   - **Return the result** stored in `dp[n]`.

4. **Time Complexity Consideration:**
   Since the dynamic programming approach iterates through each number up to `n` and checks square numbers, the time complexity is approximately `O(n * sqrt(n))`, which is efficient compared to a recursive approach.
