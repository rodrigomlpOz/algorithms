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

# Why while?
# Repeated Condition Checking: The while loop allows for continuous checking of the condition (current_sum >= target) and keeps executing as long as the condition remains true. This is necessary here because once the current_sum reaches or exceeds the target, it might still be possible to shrink the window further to achieve an even smaller valid subarray.
# Dynamic Window Adjustment: If an if statement were used, it would only perform the check and adjustment once, then move on. However, there may be cases where multiple elements need to be removed from the left side for the current_sum to fall below the target again.
