def subsetSum(nums: list[int], target: int) -> bool:
    n = len(nums)
    
    # Step 1: Initialize a 2D DP array (n+1 rows and target+1 columns)
    dp = [[False] * (target + 1) for _ in range(n + 1)]
    
    # Step 2: Base case - a sum of 0 is always possible (empty subset)
    for i in range(n + 1):
        dp[i][0] = True
    
    # Step 3: Fill the DP table
    for i in range(1, n + 1):
        for j in range(1, target + 1):
            # Exclude nums[i-1] from the subset
            dp[i][j] = dp[i-1][j]
            
            # Include nums[i-1] in the subset if it is less than or equal to j
            if j >= nums[i-1]:
                dp[i][j] = dp[i][j] or dp[i-1][j - nums[i-1]]
    
    # Step 4: Return whether the subset with the target sum is possible
    return dp[n][target]