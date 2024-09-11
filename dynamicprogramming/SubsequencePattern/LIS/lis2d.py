def lengthOfLIS_2d(nums):
    n = len(nums)
    if n == 0:
        return 0

    # Step 1: Initialize a 2D DP table, where dp[i][j] means if nums[j] can follow nums[i] in a valid subsequence
    dp = [[False] * n for _ in range(n)]

    # Initialize all subsequences ending at each element itself to be of length 1
    lengths = [1] * n

    # Step 3: Iterate over each pair of indices (i, j) where j > i
    for i in range(n):
        for j in range(i + 1, n):
            # Step 4: If nums[j] > nums[i], nums[j] can extend the subsequence ending at nums[i]
            if nums[j] > nums[i]:
                dp[i][j] = True  # Indicate that nums[j] can follow nums[i]
                lengths[j] = max(lengths[j], lengths[i] + 1)

    # Step 5: The result is the maximum length found
    return max(lengths)

# Example usage:
nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(lengthOfLIS_2d(nums))  # Output: 4 (LIS is [2, 3, 7, 101])
