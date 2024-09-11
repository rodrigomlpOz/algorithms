def canPartition(nums: list[int]) -> bool:
    total_sum = sum(nums)
    
    # If the total sum is odd, we can't split it equally
    if total_sum % 2 != 0:
        return False
    
    target = total_sum // 2
    n = len(nums)
    
    # Step 1: Create a DP array, dp[j] represents if we can achieve sum j
    dp = [False] * (target + 1)
    dp[0] = True  # A sum of 0 is always achievable (by taking no elements)
    
    # Step 2: Process each number in nums
    for num in nums:
        # Step 3: Update dp array from right to left (to prevent overwriting results)
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]  # Include or exclude the current number
    
    # Step 4: The result is whether we can achieve the target sum
    return dp[target]

# Example calls:
print(canPartition([1, 5, 11, 5]))  # Output: True
print(canPartition([1, 2, 3, 5]))   # Output: False
