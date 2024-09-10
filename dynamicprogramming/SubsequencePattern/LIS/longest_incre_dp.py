def lengthOfLIS(nums):
    # If the input array is empty, return 0 as there is no subsequence
    if not nums:
        return 0
    
    # Initialize dp array, where dp[i] represents the length of the longest increasing subsequence ending at index i.
    # Each element starts as 1, because each element alone is an increasing subsequence of length 1.
    dp = [1] * len(nums)

    # Loop through each element in the array starting from the second element (index 1)
    for i in range(1, len(nums)):
        # For each element nums[i], check all the previous elements nums[j] where j < i
        for j in range(i):
            # If nums[i] is greater than nums[j], it can extend the increasing subsequence ending at j
            if nums[i] > nums[j]:
                # Update dp[i] to the maximum value of itself or dp[j] + 1 (the length of the subsequence ending at j plus nums[i])
                dp[i] = max(dp[i], dp[j] + 1)
    
    # Return the maximum value in the dp array, which represents the length of the longest increasing subsequence
    return max(dp)
