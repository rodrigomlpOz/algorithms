def longest_palindrome_subseque(s):
    """
    Function to find the length of the longest palindromic subsequence in a string using recursion.

    Args:
    s: str - Input string.

    Returns:
    int - Length of the longest palindromic subsequence.
    """
    
    def recurse(i, j):
        # Base case: if there's one character, it's a palindrome of length 1
        if i == j:
            return 1
        # Base case: if the indices cross, there's no valid subsequence
        if i > j:
            return 0
        # If characters at i and j are the same
        if s[i] == s[j]:
            return 2 + recurse(i + 1, j - 1)
        # If characters are different, consider both excluding i or j
        else:
            return max(recurse(i + 1, j), recurse(i, j - 1))
    
    return recurse(0, len(s) - 1)
