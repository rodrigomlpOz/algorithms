def lengthOfLIS(nums):
    def max_lis(idx, cur_max):
        if idx == len(nums):
            return 0
        if nums[idx] > cur_max:
            return max(1 + max_lis(idx + 1, nums[idx]), max_lis(idx + 1, cur_max))
        return max_lis(idx + 1, cur_max)
    return max_lis( 0, float('-inf') )


arr = [10,9,2,5]
lengthOfLIS(arr)