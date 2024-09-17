def contains_duplicate(nums: list[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True  # Duplicate found
        seen.add(num)
    return False  # No duplicates found
