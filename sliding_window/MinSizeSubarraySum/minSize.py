def minSubArrayLen(target: int, nums: list[int]) -> int:
    left = 0
    current_sum = 0
    min_length = float("inf")

    for right in range(len(nums)):
        current_sum += nums[right]

        # Shrink the window from the left as long as the sum is >= target
        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= nums[left]
            left += 1

    return min_length if min_length != float("inf") else 0