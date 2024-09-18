from typing import List

def removeDuplicates(nums: List[int]) -> int:
    """
    Removes duplicates from the sorted array nums such that each element appears at most twice.
    Modifies nums in-place and returns the new length k.

    :param nums: List[int] - The input sorted array
    :return: int - The length of the array after removing extra duplicates
    """
    n = len(nums)
    if n <= 2:
        return n

    write = 2  # Start writing from the third position

    for i in range(2, n):
        # If the current element is not equal to the element at write - 2,
        # it means it can be placed at the write position
        if nums[i] != nums[write - 2]:
            nums[write] = nums[i]
            write += 1

    return write
