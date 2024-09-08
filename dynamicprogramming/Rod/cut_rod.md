### Problem Description:
The **Rod Cutting Problem** is about maximizing the profit from cutting a rod of length `n`. Given a rod of length `n` and a list `price[]` where `price[i]` is the price of a rod of length `i+1`, you can cut the rod into smaller pieces. Each piece can have its own price, and the goal is to determine the maximum revenue obtainable by cutting the rod and selling the pieces.

### Function Definition:
```python
def rodCutting(price, n):
    """
    Solves the rod cutting problem using dynamic programming.

    Args:
    price : list : List of prices where price[i] is the price of a rod of length i+1.
    n : int : The length of the rod.

    Returns:
    int : The maximum profit obtainable by cutting the rod into pieces.
    """
    # Logic to be implemented below
    pass
```

### Function Calls:
```python
# Example calls to test the rodCutting function

price = [1, 5, 8, 9, 10, 17, 17, 20]  # Prices for rod lengths from 1 to 8
n = 8  # Total length of the rod
print(rodCutting(price, n))  # Expected output: 22

price = [3, 5, 8, 9, 10, 17, 17, 20]
n = 5
print(rodCutting(price, n))  # Expected output: 13
```

### High-Level Solution Description:

The **Rod Cutting problem** is a variation of the **0-1 Knapsack problem** where the goal is to maximize the revenue by cutting a rod into smaller pieces. We approach this problem using **dynamic programming** by breaking it down into subproblems.

1. **Define the DP Table:**
   - Let `dp[i][j]` represent the maximum profit that can be obtained by cutting a rod of length `j` using the first `i` possible piece lengths.
   - The table will be of size `(n + 1) x (n + 1)`, where `n` is the length of the rod.

2. **Base Cases:**
   - If the length of the rod is 0, no revenue can be obtained, so we initialize `dp[i][0] = 0` for all `i`.
   - If no pieces are available (`i = 0`), the maximum revenue is also `0`, so initialize `dp[0][j] = 0` for all `j`.

3. **Recurrence Relation:**
   - For each piece of length `i`, we have two choices:
     - **Include the piece**: If the piece length `i` can fit into the rod of length `j`, we add the value of this piece `price[i-1]` and check the remaining rod length (`j - i`).
     - **Exclude the piece**: Move to the next piece without cutting the rod at length `i`.
   - The relation is:
     \[
     dp[i][j] = \max(\text{price}[i-1] + dp[i][j-i], dp[i-1][j])
     \]
   - Here, `price[i-1]` is the price of cutting the rod at length `i` and `dp[i][j-i]` is the maximum value for the remaining rod length `j-i`.

4. **Iterating to Fill the DP Table:**
   - We iterate over all possible piece lengths `i` (from 1 to `n`) and over all possible rod lengths `j` (from 1 to `n`).
   - For each cell `dp[i][j]`, we compute the maximum revenue either by including or excluding the current piece of length `i`.

5. **Return the Result:**
   - The final result is stored in `dp[n][n]`, which represents the maximum profit for cutting a rod of length `n` using all possible piece lengths.

---
