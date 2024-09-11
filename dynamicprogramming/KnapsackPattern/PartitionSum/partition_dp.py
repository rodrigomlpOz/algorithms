def canPartition(nums: list[int]) -> bool:
    total_sum = sum(nums)
    
    # If the total sum is odd, we can't split it equally
    if total_sum % 2 != 0:
        return False
    
    target = total_sum // 2
    n = len(nums)
    
    # Step 1: Create a DP table, dp[i][j] represents if we can achieve sum j with the first i elements
    dp = [[False] * (target + 1) for _ in range(n + 1)]
    
    # Step 2: Initialize dp[i][0] = True for all i, because a sum of 0 is always achievable (by taking no elements)
    for i in range(n + 1):
        dp[i][0] = True
    
    # Step 3: Fill the DP table
    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if nums[i-1] <= j:  # If the current number can be included
                dp[i][j] = dp[i-1][j] or dp[i-1][j - nums[i-1]]  # Include or exclude the current number
            else:
                dp[i][j] = dp[i-1][j]  # Exclude the current number
    
    # Step 4: The result is whether we can achieve the target sum using all elements
    return dp[n][target]

# Example calls:
print(canPartition([1, 5, 11, 5]))  # Output: True
print(canPartition([1, 2, 3, 5]))   # Output: False
