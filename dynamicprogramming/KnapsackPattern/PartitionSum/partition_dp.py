def canPartition(nums: list[int]) -> bool:
    total_sum = sum(nums)
    
    # If the total sum is odd, we can't split it equally
    if total_sum % 2 != 0:
        return False
    
    target = total_sum // 2
    
    # Initialize a DP array of size target + 1
    dp = [False] * (target + 1)
    dp[0] = True  # Base case: A subset sum of 0 is always possible
    
    # Loop through each number in nums
    for num in nums:
        # Traverse dp array backwards to avoid overwriting
        for i in range(target, num - 1, -1):
            dp[i] = dp[i] or dp[i - num]
    
    # Return whether we can form the subset with sum equal to target
    return dp[target]

# Example calls:
print(canPartition([1, 5, 11, 5]))  # Output: True
print(canPartition([1, 2, 3, 5]))   # Output: False
