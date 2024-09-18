def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    # Initialize three pointers
    p1 = m - 1  # Pointer for nums1
    p2 = n - 1  # Pointer for nums2
    p = m + n - 1  # Pointer for the final merged array in nums1

    # Merge nums1 and nums2 from the end
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1

    # If there are remaining elements in nums2, place them in nums1
    # No need to check for nums1 since it is already in place
    nums1[:p2 + 1] = nums2[:p2 + 1]