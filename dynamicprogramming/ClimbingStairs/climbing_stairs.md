### Problem Statement:
You are climbing a staircase. It takes `n` steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

### Function Definition:
```python
class Solution:
    def climbStairs(self, n: int) -> int:
        # Logic to be defined
        pass
```

### Function Calls:
```python
solution = Solution()

# Example test cases
print(solution.climbStairs(2))  # Expected output: 2 (ways: [1+1], [2])
print(solution.climbStairs(3))  # Expected output: 3 (ways: [1+1+1], [1+2], [2+1])
print(solution.climbStairs(4))  # Expected output: 5 (ways: [1+1+1+1], [1+1+2], [1+2+1], [2+1+1], [2+2])
print(solution.climbStairs(5))  # Expected output: 8 (ways: [1+1+1+1+1], [1+1+1+2], [1+1+2+1], [1+2+1+1], [2+1+1+1], [1+2+2], [2+1+2], [2+2+1])
```

### High-Level Explanation:
1. **Base Cases**: 
   - If there is only 1 step, there's only 1 way to reach the top.
   - If there are 2 steps, there are 2 distinct ways to reach the top: either take two 1-step moves or one 2-step move.

2. **Recursive Structure**:
   - The number of ways to reach the `n`th step is the sum of the ways to reach the `(n-1)`th step and the `(n-2)`th step, because from those positions, you can take either a 1-step or 2-step to reach the `n`th step.

3. **Dynamic Programming Approach**:
   - Use an array or variables to store intermediate results to avoid recalculating the same values multiple times (bottom-up approach).
