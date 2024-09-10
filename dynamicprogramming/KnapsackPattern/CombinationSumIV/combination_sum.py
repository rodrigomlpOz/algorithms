def combinationSum2D(nums: List[int], target: int) -> int:
    n = len(nums)
    
    # Initialize dp array where dp[i][j] means the number of ways to get sum j using first i numbers
    dp = [[0] * (target + 1) for _ in range(n + 1)]
    
    # Base case: There's exactly one way to make sum 0 (by using no elements)
    for i in range(n + 1):
        dp[i][0] = 1
    
    # Fill the dp array
    for i in range(1, n + 1):
        for j in range(1, target + 1):
            # Exclude the current number
            dp[i][j] = dp[i-1][j]
            # Include the current number if it's not greater than the current sum
            if j >= nums[i-1]:
                dp[i][j] += dp[i][j - nums[i-1]]
    
    return dp[n][target]
