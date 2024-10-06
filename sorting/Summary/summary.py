def summary_ranges(nums):
    if not nums:
        return []

    ranges = []
    start = nums[0]
    end = nums[0]

    for i in range(1, len(nums)):
        if nums[i] == nums[i-1] + 1:
            end = nums[i]
        else:
            if start == end:
                ranges.append(str(start))
            else:
                ranges.append(f"{start}->{end}")
            start = nums[i]
            end = nums[i]

    if start == end:
        ranges.append(str(start))
    else:
        ranges.append(f"{start}->{end}")

    return ranges

print(summary_ranges([0,1,2,4,5,7]))


