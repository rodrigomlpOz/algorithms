def rob(nums: List[int]) -> int:
    # Helper function to compute the maximum amount of money for houses in a linear arrangement
    def rob_linear(houses):
        n = len(houses)
        if n == 0:
            return 0
        if n == 1:
            return houses[0]
        dp = [0] * n
        dp[0] = houses[0]
        dp[1] = max(houses[0], houses[1])
        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + houses[i])
        return dp[-1]
    
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]
    
    # Case 1: Rob houses from index 0 to n-2 (excluding the last house)
    case1 = rob_linear(nums[:-1])
    # Case 2: Rob houses from index 1 to n-1 (excluding the first house)
    case2 = rob_linear(nums[1:])
    
    # Return the maximum of the two cases
    return max(case1, case2)