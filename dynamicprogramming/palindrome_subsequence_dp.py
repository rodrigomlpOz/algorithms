def longest_palindrome_subseque(s):
    """
    Function to find the length of the longest palindromic subsequence in a string.

    Args:
    s: str - Input string.

    Returns:
    int - Length of the longest palindromic subsequence.
    """
    n = len(s)
    dp = [[0]*(n) for _ in range(n)]  # Initialize the DP table
    
    # Base case: Single character palindromes
    for i in range(n):
        dp[i][i] = 1

    # Fill the DP table from bottom-right to top-left
    for i in range(n-1, -1, -1):
        for j in range(i+1, n):
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i][j-1], dp[i+1][j])

    # The result is the length of the longest palindromic subsequence for the entire string
    return dp[0][n-1]
