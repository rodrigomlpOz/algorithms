### Problem Statement:

You are given an array `nums` representing `n` balloons. Each balloon is painted with a number on it. You are asked to burst all the balloons. If you burst a balloon `i`, you will get points equal to `nums[i-1] * nums[i] * nums[i+1]`. Here, `nums[-1]` and `nums[n]` are considered to be 1 (out of bounds balloons).

Your goal is to maximize the total points you can get by bursting the balloons in an optimal order.

### Example 1:

```text
Input: nums = [3, 1, 5, 8]
Output: 167
Explanation: 
nums = [3, 1, 5, 8] --> Burst balloon 1 (1*3*5 = 15) --> nums = [3, 5, 8]
                --> Burst balloon 5 (3*5*8 = 120) --> nums = [3, 8]
                --> Burst balloon 3 (1*3*8 = 24) --> nums = [3]
                --> Burst balloon 3 (1*3*1 = 3) --> nums = []
                Total points = 15 + 120 + 24 + 8 = 167.
```

### Function Definition:

```python
def maxCoins(nums: list[int]) -> int:
    # Function logic goes here
    pass

# Example calls:
print(maxCoins([3, 1, 5, 8]))  # Output: 167
```

---

### High-Level Solution:

The problem is challenging because the order in which we burst the balloons affects the score. A **recursive or brute force** solution would try every possible bursting order, but this becomes too slow as the size of `nums` increases.

Thus, we can use **Dynamic Programming (DP)** to optimize the solution.

#### Key Observations:
1. **Boundary Conditions**: The balloons on the boundary are effectively `1` (we pretend there's a `1` balloon to the left of the first balloon and to the right of the last balloon).
   
2. **Subproblems**: For any subarray of balloons `i` to `j`, the problem of bursting all the balloons in that range can be broken down into smaller subproblems. The key is to figure out the **last balloon** to burst in a subarray, which maximizes the coins for that subproblem.

3. **Recursive Structure**:
   - The idea is to use a DP table where `dp[left][right]` stores the maximum coins we can collect by bursting all balloons between `left` and `right` (excluding the boundaries).

   - For each subproblem defined by `left` and `right`, we consider every balloon `k` between `left` and `right` as the **last balloon** to burst, which gives us:
     - Coins from bursting `k`: `nums[left-1] * nums[k] * nums[right+1]`.
     - Plus, the maximum coins we can get from subproblems: `dp[left][k-1]` and `dp[k+1][right]`.

4. **Base Case**:
   - When `left > right`, there are no balloons to burst, so the result is 0 for such subproblems.

5. **Final Answer**:
   - The answer will be stored in `dp[1][n]` where `n` is the number of balloons after including the boundaries (i.e., after padding `nums` with `1` at both ends).

---

### Dynamic Programming Solution:

```python
def maxCoins(nums: list[int]) -> int:
    # Step 1: Pad the nums array with 1 at both ends (left and right)
    nums = [1] + nums + [1]
    n = len(nums)
    
    # Step 2: Initialize the DP table where dp[i][j] represents the max coins obtained
    # from bursting balloons in the range (i, j) (exclusive of i and j)
    dp = [[0] * n for _ in range(n)]
    
    # Step 3: Build the DP table. We work backwards, considering all possible ranges
    for length in range(2, n):  # length is the size of the subproblem
        for left in range(0, n - length):  # left boundary of the subproblem
            right = left + length  # right boundary of the subproblem
            # Try bursting each balloon between left and right as the last balloon
            for k in range(left + 1, right):
                dp[left][right] = max(
                    dp[left][right],
                    dp[left][k] + dp[k][right] + nums[left] * nums[k] * nums[right]
                )
    
    # Step 4: Return the result for the whole array (excluding padded boundaries)
    return dp[0][n-1]

# Example calls:
print(maxCoins([3, 1, 5, 8]))  # Output: 167
```

---

### Detailed Explanation:

1. **Padding the Array**:
   - We add a `1` at both ends of the `nums` array. This makes handling edge cases easier because we now don't need to worry about the out-of-bounds cases when bursting the leftmost or rightmost balloons.
   - If `nums = [3, 1, 5, 8]`, after padding it becomes `nums = [1, 3, 1, 5, 8, 1]`.

2. **DP Table Definition**:
   - We define `dp[left][right]` as the maximum coins that can be obtained by bursting all the balloons between `left` and `right` (exclusive). Initially, all values in `dp` are set to 0.

3. **Filling the DP Table**:
   - For every subarray of balloons, we choose one balloon `k` (between `left` and `right`) to be the last one burst. The coins obtained from bursting balloon `k` would be `nums[left] * nums[k] * nums[right]`.
   - After bursting `k`, we have two subproblems: one involving the balloons on the left of `k` (`dp[left][k]`), and one involving the balloons on the right of `k` (`dp[k][right]`).
   - We iterate over all possible lengths of subarrays (from size 2 up to the full array), and for each subarray, we test all possible choices for the last balloon to burst.

4. **Final Result**:
   - The final result is stored in `dp[0][n-1]`, which represents the maximum coins that can be obtained by bursting all the balloons (including the boundary `1`s).

---

### Time and Space Complexity:

- **Time Complexity**: `O(n^3)`, where `n` is the length of the padded `nums` array. For each pair `(left, right)`, we perform an inner loop to iterate through each possible balloon `k`, resulting in cubic complexity.
  
- **Space Complexity**: `O(n^2)`, since we use a 2D DP table of size `n x n`.

---

### Key Points:
- The idea is to break the problem down into subproblems by figuring out the best last balloon to burst in any given range.
- Using DP allows us to solve the problem optimally by considering all possible subranges and choices for the last balloon to burst.
- The complexity is acceptable for typical input sizes (up to a few hundred balloons).
