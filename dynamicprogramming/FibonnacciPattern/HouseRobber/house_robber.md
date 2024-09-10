### Problem Statement:
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. However, you cannot rob two adjacent houses because they will trigger an alarm. Given a list of non-negative integers `nums` where each integer represents the amount of money in each house, determine the maximum amount of money you can rob without triggering the alarm.

### Function Definition:
```python
def house_robber(nums):
    pass
```

### Function Calls:

```python
# Test cases
print(house_robber([1, 2, 3, 1]))  # Expected output: 4 (rob house 1 and house 3)
print(house_robber([2, 7, 9, 3, 1]))  # Expected output: 12 (rob house 1, 3, and 5)
print(house_robber([0]))  # Expected output: 0 (only one house with no money)
print(house_robber([2, 3, 2]))  # Expected output: 3 (rob house 2)
```

### High-Level Solution:
1. **Base cases**: If there are no houses, return `0`. If there is only one house, return the amount in that house.
2. **Dynamic Programming Approach**:
    - Use a list `dp` where `dp[i]` holds the maximum amount of money you can rob up to house `i`.
    - Initialize the first house as the maximum money available from that house.
    - For the second house, choose the maximum between the first and second house.
3. **Filling the `dp` array**:
    - For each subsequent house `i`, you decide whether to:
      - Rob the current house `i` and add it to the best solution two houses back (`dp[i-2]`).
      - Skip the current house and take the best solution up to the previous house (`dp[i-1]`).
    - Take the maximum of these two options for each house.
4. **Final Solution**: The value at `dp[-1]` (last element in the `dp` array) will give the maximum amount that can be robbed.
