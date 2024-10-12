def rotate(nums: list[int], k: int) -> None:
    """
    Rotates the array 'nums' to the right by 'k' steps in-place.

    Args:
    nums (List[int]): The list of integers to rotate.
    k (int): The number of steps to rotate the array.

    Returns:
    None: The function modifies the list in-place.
    """
    n = len(nums)
    k %= n  # Normalize k

    def reverse(sub_nums, start, end):
        while start < end:
            sub_nums[start], sub_nums[end] = sub_nums[end], sub_nums[start]
            start += 1
            end -= 1

    # Step 1: Reverse the entire array
    reverse(nums, 0, n - 1)
    # Step 2: Reverse the first k elements
    reverse(nums, 0, k - 1)
    # Step 3: Reverse the remaining n - k elements
    reverse(nums, k, n - 1)