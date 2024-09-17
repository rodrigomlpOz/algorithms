def longestConsecutive(self, nums: list[int]) -> int:
    """
    Function to return the length of the longest consecutive sequence.

    :param nums: List[int] - The input list of integers.
    :return: int - The length of the longest consecutive sequence.
    """

    # Return 0 if the list is empty
    if not nums:
        return 0

    # Step 1: Convert the list to a set to remove duplicates and allow O(1) lookups
    num_set = set(nums)
    longest_streak = 0

    # Step 2: Iterate through the set
    for num in num_set:
        # Check if it's the start of a sequence (i.e., num - 1 is not in the set)
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            # Step 3: Count the consecutive numbers
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            # Step 4: Update the longest streak found
            longest_streak = max(longest_streak, current_streak)

    return longest_streak