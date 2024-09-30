def summaryRanges(nums):
    # Base case: empty array
    if not nums:
        return []
    
    ranges = []
    start = nums[0]
    
    for i in range(1, len(nums)):
        # If the current number is not consecutive
        if nums[i] != nums[i - 1] + 1:
            if start == nums[i - 1]:
                ranges.append(str(start))
            else:
                ranges.append(f"{start}->{nums[i - 1]}")
            start = nums[i]
    
    # Add the final range
    if start == nums[-1]:
        ranges.append(str(start))
    else:
        ranges.append(f"{start}->{nums[-1]}")
    
    return ranges
