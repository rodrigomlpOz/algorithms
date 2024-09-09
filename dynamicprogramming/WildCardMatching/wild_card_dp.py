def isMatch(s: str, p: str) -> bool:
    m, n = len(s), len(p)
    
    # DP table where dp[i][j] means s[:i] matches p[:j]
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    
    # Base case: both strings are empty
    dp[0][0] = True
    
    # Initialize the first row (matching an empty string with a pattern)
    for j in range(1, n + 1):
        if p[j-1] == '*':
            dp[0][j] = dp[0][j-1]
    
    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j-1] == '*':
                # '*' matches zero characters or at least one character
                dp[i][j] = dp[i-1][j] or dp[i][j-1]
            elif p[j-1] == '?' or p[j-1] == s[i-1]:
                # '?' matches any one character or the current characters match
                dp[i][j] = dp[i-1][j-1]
    
    # Return whether the entire string matches the entire pattern
    return dp[m][n]
