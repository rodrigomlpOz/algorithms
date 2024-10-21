def max_sum_subarray_of_size_k(k: int, arr: list[int]) -> int:
    max_sum = float('-inf')
    window_sum = 0
    left = 0

    for right in range(len(arr)):
        window_sum += arr[right]

        # Once we have a window of size k, start updating the max_sum
        if right >= k - 1:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[left]  # Slide the window by removing the element at the left
            left += 1

    return max_sum