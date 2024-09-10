def longestPalindrome(s: str) -> str:
    n = len(s)
    if n == 0:
        return ""
    
    dp = [[False] * n for _ in range(n)]  # DP table to store palindromic status
    start = 0  # Starting index of the longest palindrome
    max_length = 1  # Maximum length of the longest palindrome found
    
    # Base case: every single character is a palindrome
    for i in range(n):
        dp[i][i] = True
    
    # Fill the DP table for substrings of length >= 2
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                if length == 2 or dp[i+1][j-1]:
                    dp[i][j] = True
                    if length > max_length:
                        max_length = length
                        start = i
    
    # Return the longest palindromic substring
    return s[start:start + max_length]
