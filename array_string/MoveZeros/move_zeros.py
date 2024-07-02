def moveZeroes(nums):
    lastNonZeroFoundAt = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[lastNonZeroFoundAt] = nums[i]
            lastNonZeroFoundAt += 1
    
    for j in range(lastNonZeroFoundAt, len(nums)):
        nums[j] = 0
