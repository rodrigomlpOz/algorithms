from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
    """
    Finds all unique triplets in the array which gives the sum of zero.

    :param nums: List[int] - The input array of integers
    :return: List[List[int]] - A list of unique triplets that sum to zero
    """
    nums.sort()  # Step 1: Sort the array
    n = len(nums)
    result = []

    for i in range(n):
        # Skip duplicate fixed elements
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, n - 1  # Initialize two pointers

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if current_sum == 0:
                # Found a triplet
                result.append([nums[i], nums[left], nums[right]])

                # Skip duplicates for left pointer
                while left < right and nums[left] == nums[left + 1]:
                    left += 1

                # Skip duplicates for right pointer
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                # Move pointers after finding a valid triplet
                left += 1
                right -= 1

            elif current_sum < 0:
                # Need a larger sum; move the left pointer to the right
                left += 1
            else:
                # Need a smaller sum; move the right pointer to the left
                right -= 1

    return result
