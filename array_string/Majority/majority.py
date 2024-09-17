def majorityElement(nums) -> int:
    n = len(nums)
    
    for i in range(n):
        count = 0
        # Count how many times nums[i] appears in the list
        for j in range(n):
            if nums[j] == nums[i]:
                count += 1
        # If the count of this element is greater than n // 2, return it
        if count > n // 2:
            return nums[i]

    return -1  # Should never reach here, as the problem guarantees a majority element
