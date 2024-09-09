def isMatch(s: str, p: str) -> bool:
    # Create a DP table with (len(s) + 1) rows and (len(p) + 1) columns
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
    
    # Base case: both s and p are empty
    dp[0][0] = True
    
    # Handle patterns like a*, a*b*, etc. where the pattern can match an empty string
    for j in range(2, len(p) + 1):
        if p[j-1] == '*':
            dp[0][j] = dp[0][j-2]
    
    # Fill the DP table
    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            # Case 1: Current characters match or there's a '.' in the pattern
            if p[j-1] == s[i-1] or p[j-1] == '.':
                dp[i][j] = dp[i-1][j-1]
            # Case 2: Handle the '*' wildcard
            elif p[j-1] == '*':
                # Two possibilities:
                # 1. '*' acts like zero occurrences of the preceding character (dp[i][j-2])
                # 2. '*' acts like one or more occurrences of the preceding character (dp[i-1][j])
                if p[j-2] == s[i-1] or p[j-2] == '.':
                    dp[i][j] = dp[i][j-2] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i][j-2]
    
    # The answer is in dp[len(s)][len(p)]
    return dp[len(s)][len(p)]

# Example calls:
print(isMatch("aa", "a*"))  # Output: True
print(isMatch("ab", ".*"))  # Output: True
print(isMatch("aab", "c*a*b"))  # Output: True
