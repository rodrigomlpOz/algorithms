def strStr(haystack: str, needle: str) -> int:
    """
    Finds the index of the first occurrence of needle in haystack using the Sliding Window Approach.

    Parameters:
    haystack (str): The string to search within.
    needle (str): The substring to search for.

    Returns:
    int: The starting index of the first occurrence of needle in haystack, or -1 if not found.
    """
    n = len(haystack)
    m = len(needle)
    
    # Edge Case: If needle is empty, return 0
    if m == 0:
        return 0
    
    # Edge Case: If needle is longer than haystack, it cannot be found
    if m > n:
        return -1
    
    # Slide a window of size m over haystack
    for i in range(n - m + 1):
        # Compare the substring with needle
        if haystack[i:i + m] == needle:
            return i  # Match found at index i
    
    return -1  # No match found
