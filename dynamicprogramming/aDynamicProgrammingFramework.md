### Skeleton for 1D DP:

```python
def solveProblem(input_value):
    # Step 1: Initialize the DP array
    dp = [initial_value] * (size_needed_based_on_input)

    # Step 2: Define the base cases
    dp[base_case_index] = base_case_value

    # Step 3: Iterate through the problem's main range (often from 1 to input_value)
    for i in range(1, input_value + 1):
        # Step 4: Iterate through possible choices (e.g., perfect squares, previous elements, etc.)
        for choice in range(...):  # Modify this loop based on the specific problem
            # Step 5: Update the dp[i] based on recurrence relation
            dp[i] = min/max(dp[i], dp[relevant_state] + 1)  # Modify the operation based on the problem

    # Step 6: Return the result, typically stored in dp[input_value]
    return dp[input_value]

# Example usage
input_value = ...
print(solveProblem(input_value))
```

### Explanation:

1. **Step 1: Initialize the DP Array**:
   - The `dp` array is initialized with default values (`initial_value`). Typically, this might be `float('inf')` for minimization problems or `0`/`1` for maximization.
   - The size of the `dp` array depends on the problem. For instance, for **Perfect Squares**, the size is `n + 1`.

2. **Step 2: Define the Base Cases**:
   - The base cases define the simplest input(s) that have a known solution. For example, `dp[0]` is usually set to `0` for problems like **Perfect Squares** or **Coin Change**.
   
3. **Step 3: Iterate Over the Main Range**:
   - Typically, this loop runs from 1 to the given `input_value`. This is where we solve subproblems for every possible input from 1 to the target value.

4. **Step 4: Iterate Over Possible Choices**:
   - This nested loop evaluates all possible decisions or subproblems. For example, in the **Perfect Squares** problem, this would loop over all square numbers.

5. **Step 5: Apply Recurrence Relation**:
   - The core logic of dynamic programming is applied here, where the current state is updated based on previous states. For minimization problems, you typically use `min(dp[i], ...)`, and for maximization problems, you use `max(dp[i], ...)`.

6. **Step 6: Return the Result**:
   - Once the loops finish, the result is typically stored in `dp[input_value]`.


### Adapting the Skeleton:

- **Perfect Squares**: You’d loop over square numbers as choices.
- **Longest Increasing Subsequence**: You’d compare the current element to previous elements to form subsequences.
- **Coin Change**: You’d loop over coin denominations as choices.

This flexible structure will help you implement 1D DP solutions for a wide variety of problems.

### General Framework for 2D Dynamic Programming Problems:

1. **Define the DP Table:**
   - Determine how the DP table will store the state. The state typically represents the subproblem you're solving.
   - Example: In the 0-1 Knapsack problem, the DP table `K[i][w]` stores the maximum value that can be achieved with the first `i` items and capacity `w`.

2. **Initialize the DP Table:**
   - Typically, the base cases represent "empty" scenarios (e.g., no items to consider, zero capacity, or starting from the beginning).
   - Example: Initialize the first row and column to `0` in the knapsack problem because if there are no items or the capacity is 0, the maximum value is `0`.

3. **Define the Recurrence Relation:**
   - This is the core logic. It defines how you transition from one state to another and solve subproblems.
   - For each state, consider whether to include/exclude an element, move in a certain direction, or perform some other operation.
   - Example: In the knapsack problem, you decide between including an item or not:
     ```python
     K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w])
     ```

4. **Iterate to Fill the DP Table:**
   - Usually, you iterate over all possible states (in a nested loop for 2D DP) and fill the table based on previously computed values.
   - Example: For each item `i` and weight `w`, compute the maximum possible value and store it in `K[i][w]`.

5. **Return the Final Result:**
   - After filling the DP table, the solution to the original problem is stored in a specific cell of the table (often the bottom-right corner).
   - Example: In the knapsack problem, `K[n][W]` will store the result of using all `n` items with capacity `W`.


Sure! Below, I'll show how this 1D DP framework can be adapted for three different problems: **Perfect Squares**, **Longest Increasing Subsequence (LIS)**, and **Coin Change**. Each problem has unique characteristics but can follow the same skeleton.

---

### Problem 1: Perfect Squares

**Problem Statement**: Find the minimum number of perfect square numbers that sum to `n`.

**Solution**: Use 1D DP to keep track of the minimum number of perfect squares needed to sum up to every number from `1` to `n`.

```python
import math

def numSquares(n):
    # Step 1: Initialize the DP array
    dp = [float('inf')] * (n + 1)

    # Step 2: Base case: 0 can be represented by 0 squares
    dp[0] = 0

    # Precompute all square numbers less than or equal to n
    square_nums = [i**2 for i in range(1, int(math.sqrt(n)) + 1)]

    # Step 3: Iterate over all numbers from 1 to n
    for i in range(1, n + 1):
        # Step 4: For each number i, check all square numbers <= i
        for square in square_nums:
            if i < square:
                break
            # Step 5: Update the dp[i] with the minimum value
            dp[i] = min(dp[i], dp[i - square] + 1)

    # Step 6: Return the final result, dp[n]
    return dp[n]

# Example usage
print(numSquares(12))  # Output: 3 (4 + 4 + 4)
```

---

### Problem 2: Longest Increasing Subsequence (LIS)

**Problem Statement**: Find the length of the longest increasing subsequence in a given array.

**Solution**: Use 1D DP to store the length of the longest increasing subsequence that ends at each index.

```python
def lengthOfLIS(nums):
    if not nums:
        return 0

    # Step 1: Initialize the DP array
    dp = [1] * len(nums)  # Every element is a subsequence of length 1 by itself

    # Step 2: Base case: already initialized above, every element is a subsequence of length 1

    # Step 3: Iterate over each element in the array
    for i in range(1, len(nums)):
        # Step 4: For each i, check all previous elements j < i
        for j in range(i):
            if nums[i] > nums[j]:
                # Step 5: Update dp[i] with the maximum length
                dp[i] = max(dp[i], dp[j] + 1)

    # Step 6: Return the maximum value in dp (the longest subsequence length)
    return max(dp)

# Example usage
print(lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))  # Output: 4 (Subsequence: [2, 3, 7, 101])
```

---

### Problem 3: Coin Change

**Problem Statement**: Given an amount and a list of coin denominations, find the minimum number of coins needed to make the amount.

**Solution**: Use 1D DP to track the minimum number of coins needed to make each amount from `0` to `amount`.

```python
def coinChange(coins, amount):
    # Step 1: Initialize the DP array
    dp = [float('inf')] * (amount + 1)
    
    # Step 2: Base case: 0 coins are needed to make amount 0
    dp[0] = 0

    # Step 3: Iterate over each amount from 1 to 'amount'
    for i in range(1, amount + 1):
        # Step 4: For each i, check all coin denominations
        for coin in coins:
            if i >= coin:
                # Step 5: Update dp[i] with the minimum number of coins
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # Step 6: If dp[amount] is still infinity, return -1 (no solution), otherwise return dp[amount]
    return dp[amount] if dp[amount] != float('inf') else -1

# Example usage
print(coinChange([1, 2, 5], 11))  # Output: 3 (11 = 5 + 5 + 1)
```

---

### Breakdown of Similarities in the Framework:

| **Step**                      | **Perfect Squares**                                              | **LIS**                                                           | **Coin Change**                                                 |
|-------------------------------|------------------------------------------------------------------|-------------------------------------------------------------------|-----------------------------------------------------------------|
| **Step 1: Initialize DP Array**| `dp = [inf] * (n + 1)`                                           | `dp = [1] * len(nums)`                                             | `dp = [inf] * (amount + 1)`                                      |
| **Step 2: Base Case**          | `dp[0] = 0`                                                     | `dp[i] = 1` (already initialized)                                  | `dp[0] = 0`                                                     |
| **Step 3: Main Loop**          | Iterate from 1 to `n`                                            | Iterate over all elements in `nums`                                | Iterate from 1 to `amount`                                       |
| **Step 4: Choices Loop**       | Loop over square numbers                                         | Loop over all `j` where `j < i`                                    | Loop over coin denominations                                     |
| **Step 5: Recurrence Relation**| `dp[i] = min(dp[i], dp[i - square] + 1)`                         | `dp[i] = max(dp[i], dp[j] + 1)`                                    | `dp[i] = min(dp[i], dp[i - coin] + 1)`                           |
| **Step 6: Return Result**      | Return `dp[n]`                                                   | Return `max(dp)`                                                   | Return `dp[amount]` or `-1` if no solution                       |

---

### Key Observations:
- **Initialization**: Each problem initializes a DP array based on the input size.
- **Base Case**: The base case is typically for the smallest subproblem, such as `dp[0] = 0`.
- **Recurrence Relation**: The DP state is updated by either minimizing or maximizing a value, depending on the problem (e.g., minimizing coin usage or maximizing subsequence length).
- **Result**: The final result is found at the `n`th or maximum value in the DP array.

This structure allows for easy adaptation of the 1D DP framework to a variety of problems.
---

### 2D Dynamic Programming Framework Template:

```python
def solveDPProblem(params):
    # 1. Define the DP table
    dp = [[0 for _ in range(width)] for _ in range(height)]  # Adjust dimensions as needed

    # 2. Initialize the base cases
    for i in range(height):
        dp[i][0] = base_case_value  # Example for row initialization
    for j in range(width):
        dp[0][j] = base_case_value  # Example for column initialization
    
    # 3. Fill the DP table using the recurrence relation
    for i in range(1, height):   # Start from 1 if 0 is the base case
        for j in range(1, width):
            # Define the recurrence relation based on the problem
            dp[i][j] = some_function_of(dp[i-1][j], dp[i][j-1], other_params)

    # 4. Return the result stored in dp table
    return dp[height-1][width-1]  # Adjust based on the final result location
```

---

### Example of a Common 2D DP Problem: Grid Pathfinding

#### Problem:
Find the number of unique paths from the top-left corner to the bottom-right corner of a grid, moving only down or right.

#### Solution using DP:

```python
def uniquePaths(m, n):
    # 1. Define the DP table
    dp = [[0 for _ in range(n)] for _ in range(m)]

    # 2. Initialize the base cases (first row and first column to 1)
    for i in range(m):
        dp[i][0] = 1  # Only one way to reach any cell in the first column
    for j in range(n):
        dp[0][j] = 1  # Only one way to reach any cell in the first row

    # 3. Fill the DP table using the recurrence relation
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]  # Sum of paths from top and left

    # 4. Return the result stored in dp table (bottom-right corner)
    return dp[m-1][n-1]

# Test the function
m, n = 3, 3
print(uniquePaths(m, n))  # Output: 6
```

### Steps Followed in the Example:

1. **DP Table Definition:** 
   - `dp[i][j]` represents the number of ways to reach cell `(i, j)`.
   
2. **Initialization:**
   - There's only one way to reach any cell in the first row or first column, so those are initialized to 1.

3. **Recurrence Relation:**
   - To reach a cell `(i, j)`, you can come either from the cell above `(i-1, j)` or from the cell to the left `(i, j-1)`. Hence:
     ```python
     dp[i][j] = dp[i-1][j] + dp[i][j-1]
     ```

4. **Final Result:**
   - The result is stored in the bottom-right corner `dp[m-1][n-1]`.

---

### Takeaways:

- **DP Table:** Always think of the DP table as a way of storing partial results for subproblems.
- **Base Cases:** Identify what happens when the problem is "empty" or trivial.
- **Recurrence Relation:** Define how the solution to a subproblem can be derived from solutions to smaller subproblems.
- **Optimization:** Dynamic programming ensures that you avoid recalculating overlapping subproblems, making it more efficient than recursive approaches.

Let me know if you'd like more specific examples or explanations!
